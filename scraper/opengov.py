"""
Core scraping logic for OpenGov Procurement portals
"""

import time
import re
from datetime import datetime, date
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper
from scraper.browser import StealthBrowser


@register_scraper("opengov")
class OpenGovScraper(BaseScraper):
    """Scraper for OpenGov Procurement portals"""
    requires_browser = True
    
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from a portal
        
        Steps:
        1. Navigate to portal
        2. Trigger Search
        3. Increase rows per page to 50 (to capture all active projects)
        4. Extract project data
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping: {portal_name}")
        print(f"{'='*50}")
        
        # Navigate to portal
        # Navigate to portal
        if not self.browser.navigate(url):
            error_msg = f"Failed to load portal: {portal_name}"
            print(f"  ✗ {error_msg}")
            raise PortalScrapingError(error_msg)
        
        # Give the React app time to fully load - wait for search bar or table
        if not self.browser.wait_for_element(By.XPATH, "//input[@aria-label='Search']|//button[contains(text(), 'Search')]|//div[@role='row']"):
            print("  ⚠ Timed out waiting for portal to load main elements")
        
        # Step 2: Triggering search to ensure active filters are applied
        print("  Step 2: Triggering search...")
        if not self._click_search():
            print("  ⚠ Could not click search, continuing anyway...")
        
        # Wait for results to load - wait for rows OR empty state message
        # This prevents waiting full timeout when no projects exist
        try:
             WebDriverWait(self.browser.driver, 5).until(
                EC.any_of(
                    EC.presence_of_element_located((By.XPATH, "//div[@role='row']")),
                    EC.presence_of_element_located((By.XPATH, "//tr")),
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No records found')]")),
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No active projects')]")),
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No Projects Found')]")),
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Please try a different search query')]"))
                )
            )
        except TimeoutException:
            pass # Continue to extraction even if timeout, might be empty or using fallback
        
        # Step 3: Increase rows per page to 50
        # Optimization: Scan everything on one page since we compare against database
        print("  Step 3: Increasing rows per page to 50...")
        self._set_rows_per_page(50)

        # Step 4: Extract projects
        print("  Step 4: Extracting projects...")
        projects = self._extract_projects(portal_key)
        
        print(f"  ✓ Found {len(projects)} active projects")
        return projects
    

    def _select_active_filter(self) -> bool:
        """Click the Active status filter"""
        # Check if already active
        try:
            current_status = self.browser.find_elements(By.XPATH, "//div[contains(@class, 'react-select__single-value')]")
            for status in current_status:
                if "Active" in status.text:
                    print("    ✓ Filter is already set to 'Active'")
                    return True
        except Exception:
            pass
            
        # Try multiple selectors for the Active button/checkbox
        selectors = [
            # React Select Control (click to open if needed, but we might just need to verify)
            "//div[contains(@class, 'react-select__control')]//div[contains(text(), 'Active')]",
            # Button with text "Active"
            "//button[contains(text(), 'Active')]",
            "//span[contains(text(), 'Active')]/parent::button",
            # Chip/tag style
            "//div[contains(@class, 'chip') and contains(text(), 'Active')]",
            # Checkbox or radio
            "//label[contains(text(), 'Active')]",
            "//input[@value='active']/parent::label",
            # Status dropdown option
            "//li[contains(text(), 'Active')]",
            "//div[@role='option' and contains(text(), 'Active')]",
            # Generic clickable with Active text
            "//*[contains(@class, 'status') and contains(text(), 'Active')]",
        ]
        
        for selector in selectors:
            try:
                elements = self.browser.find_elements(By.XPATH, selector)
                print(f"    Searching for Active filter with: {selector}")
                for elem in elements:
                    if elem.is_displayed():
                        print(f"    ✓ Found and clicking: {selector}")
                        elem.click()
                        # Wait for the click to process - usually results in a URL change or UI update
                        # But since we have other waits downstream, we can just return true
                        return True
            except Exception as e:
                print(f"    ⚠ Error checking selector {selector}: {e}")
                continue
        
        return False
    
    def _sort_by_release_date(self) -> bool:
        """Double-click Release Date header to sort descending (newest first)"""
        # 0. Check for empty state first to save time
        try:
            source = self.browser.get_page_source()
            if "No records found" in source or "No active projects" in source or "No Projects Found" in source:
                print("      ✓ No active projects found - skipping sort")
                return True
        except Exception:
            pass

        # Prioritize the most common selectors found in OpenGov
        selectors = [
            # 1. Standard Opengov React Table Header
            "//div[@role='columnheader']//div[contains(text(), 'Release Date')]",
            "//div[contains(@class, 'rt-resizable-header-content') and contains(text(), 'Release Date')]",
            # 2. Button/Sortable Header
            "//button[contains(text(), 'Release Date')]",
            "//th[contains(text(), 'Release')]",
            # 3. Generic fallback
            "//*[contains(text(), 'Release Date')]",
        ]
        
        for selector in selectors:
            try:
                elements = self.browser.find_elements(By.XPATH, selector)
                
                # Filter for visible elements
                visible_elements = [e for e in elements if e.is_displayed()]
                
                if not visible_elements:
                    continue
                    
                target = visible_elements[0]
                print(f"      ✓ Found visible header")
                
                # Click 1 — triggers ascending sort
                # We want to capture the state of the table before clicking to wait for it to go stale
                # This ensures the sort has actually processed
                try:
                    table_rows = self.browser.driver.find_elements(By.XPATH, "//div[@role='row']")
                    first_row = table_rows[0] if table_rows else target
                except Exception:
                    first_row = target

                try:
                    target.click()
                except Exception:
                    self.browser.driver.execute_script("arguments[0].click();", target)
                
                # Wait for React to re-render (element reference becomes stale)
                try:
                    WebDriverWait(self.browser.driver, 2).until(EC.staleness_of(first_row))
                except TimeoutException:
                    pass # Might not have refreshed yet or didn't need to

                
                # Click 2 — switches to descending sort (newest first)
                # Re-find because DOM was re-rendered by the sort
                # Use a short wait loop for the re-appearance
                target = None
                for _ in range(3):
                    try:
                        elements_retry = self.browser.find_elements(By.XPATH, selector)
                        visible_retry = [e for e in elements_retry if e.is_displayed()]
                        if visible_retry:
                            target = visible_retry[0]
                            break
                    except Exception:
                        pass
                    time.sleep(0.5)

                if target:
                    try:
                        # Capture row again for staleness check
                        try:
                            table_rows = self.browser.driver.find_elements(By.XPATH, "//div[@role='row']")
                            first_row = table_rows[0] if table_rows else target
                        except Exception:
                            first_row = target
                            
                        try:
                            target.click()
                        except Exception:
                            self.browser.driver.execute_script("arguments[0].click();", target)
                            
                        print("      ✓ Sorted by release date (Double Clicked)")
                        
                        # Wait for the second sort to process
                        try:
                            WebDriverWait(self.browser.driver, 2).until(EC.staleness_of(first_row))
                        except TimeoutException:
                            pass
                            
                        return True
                    except Exception as e:
                        print(f"      ⚠ Error on second click: {e}")
                else:
                    print("      ⚠ Could not re-find header for second click")
                
            except Exception as e:
                continue
                
        # Check if the table is empty (No records found)
        try:
            source = self.browser.get_page_source()
            if "No records found" in source or "No active projects" in source:
                print("      ✓ No active projects found - skipping sort")
                return True
        except Exception:
            pass
        
        return False
    
    def _set_rows_per_page(self, count: int = 40) -> bool:
        """Find the rows per page dropdown and select the target count"""
        try:
            # Capture a reference to the current table content to check for updates
            old_first_row = None
            try:
                old_rows = self.browser.driver.find_elements(By.XPATH, "//div[@role='row']")
                if old_rows:
                    old_first_row = old_rows[0]
            except Exception:
                pass

            # Dropdown is usually a <select> or a React-Select div near the bottom
            # Based on user screenshot, it contains the text "10 rows"
            selectors = [
                "//select[contains(@aria-label, 'rows per page')]",
                "//div[contains(@class, 'select')]//div[contains(text(), 'rows')]",
                "//span[contains(text(), 'rows')]/parent::div",
                "//select", # Generic fallback
            ]
            
            for selector in selectors:
                try:
                    elements = self.browser.find_elements(By.XPATH, selector)
                    for elem in elements:
                        if elem.is_displayed():
                            clicked = False
                            if elem.tag_name == "select":
                                from selenium.webdriver.support.ui import Select
                                select = Select(elem)
                                # Try to find option with '40' or max available
                                options = [o.text for o in select.options]
                                target_val = str(count)
                                if target_val in options:
                                    select.select_by_visible_text(target_val)
                                else:
                                    # Fallback to last option (usually max)
                                    select.select_by_index(len(options) - 1)
                                clicked = True
                            else:
                                # It's a div/custom dropdown
                                elem.click()
                                time.sleep(0.5) # Short wait for dropdown animation
                                # Look for the option in the list
                                option_xpath = f"//div[@role='option' and contains(text(), '{count}')]"
                                options = self.browser.find_elements(By.XPATH, option_xpath)
                                if options:
                                    options[0].click()
                                    clicked = True
                                else:
                                    # Try generic any option that looks like a number > 10
                                    generic_options = self.browser.find_elements(By.XPATH, "//div[@role='option']")
                                    for opt in generic_options:
                                        if any(x in opt.text for x in ['40', '50', '100']):
                                            opt.click()
                                            clicked = True
                                            break
                            
                            if clicked:
                                # Wait for table update if we had rows
                                if old_first_row:
                                    try:
                                        # 1. Wait for old row to disappear (stale)
                                        WebDriverWait(self.browser.driver, 5).until(EC.staleness_of(old_first_row))
                                        # 2. Wait for new rows to appear (presence)
                                        WebDriverWait(self.browser.driver, 5).until(
                                            EC.presence_of_element_located((By.XPATH, "//div[@role='row']"))
                                        )
                                        # 3. Small buffer for render completion
                                        time.sleep(0.5)
                                    except TimeoutException:
                                        print("    ⚠ Table did not refresh properly after changing rows per page (timeout)")
                                else:
                                    # If no rows before, just wait for new rows
                                    try:
                                        WebDriverWait(self.browser.driver, 5).until(
                                            EC.presence_of_element_located((By.XPATH, "//div[@role='row']"))
                                        )
                                    except TimeoutException:
                                        time.sleep(2) # Fallback sleep if no rows appear

                                return True
                except Exception:
                    continue
            return False
        except Exception as e:
            print(f"    ⚠ Error setting rows per page: {e}")
            return False

    def _click_search(self) -> bool:
        """Click the Search button"""
        selectors = [
            "//button[contains(text(), 'Search')]",
            "//button[@type='submit']",
            "//input[@type='submit']",
            "//button[contains(@class, 'search')]",
            "//*[@aria-label='Search']",
        ]
        
        for selector in selectors:
            try:
                elements = self.browser.find_elements(By.XPATH, selector)
                for elem in elements:
                    if elem.is_displayed():
                        elem.click()
                        # No sleep needed, we rely on the subsequent result waiting
                        return True
            except Exception:
                continue
        
        return False
    
    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Extract project data from the results table/list"""
        projects = []
        
        # Try to find project rows in various table/list structures
        row_selectors = [
            "//div[@role='row']", # Explicitly confirmed for Phoenix
            "//tr[contains(@class, 'row')]",
            "//div[contains(@class, 'rt-tr-group')]", # Common React-Table group
            "//div[contains(@class, 'project-row')]",
            "//div[contains(@class, 'solicitation')]",
            "//a[contains(@href, '/portal/') and contains(@href, '/projects/')]",
            "//table//tbody//tr",
            "//div[contains(@class, 'list-item')]",
        ]
        
        for selector in row_selectors:
            try:
                rows = self.browser.find_elements(By.XPATH, selector)
                if rows:
                    print(f"    Found {len(rows)} rows with selector: {selector[:50]}...")
                    for row in rows:
                        project = self._parse_project_row(row, portal_key)
                        if project:
                            projects.append(project)
                    if projects:
                        break
            except Exception as e:
                continue
        
        # If no structured data, try to extract from page source
        if not projects:
            projects = self._extract_from_page_source(portal_key)
        
        return projects
    
    def _parse_project_row(self, row, portal_key: str) -> Optional[Project]:
        """Parse a single project row - simplified to only extract title and ID"""
        try:
            # Get all text content
            text = row.text.strip()
            if not text or len(text) < 10:
                return None
            
            # Try to find a link for the project URL
            url = None
            try:
                link = row.find_element(By.TAG_NAME, "a")
                url = link.get_attribute("href")
            except NoSuchElementException:
                pass
            
            # Try to extract structured data
            # Look for common patterns in the text
            lines = text.split('\n')
            
            # First line is usually the title
            title = lines[0] if lines else text[:100]
            
            # SKIP HEADERS: If the title is "Project Title" or "ID", it's a header row
            if title.lower() in ["project title", "id", "title"]:
                return None
    

            # Try to extract the true internal ID from the URL first (most stable)
            # URL format: https://procurement.opengov.com/portal/portal_key/projects/232196
            if url and "/projects/" in url:
                url_id = url.split("/projects/")[-1].split("?")[0].split("#")[0]
                if url_id and url_id.isdigit():
                    project_id = url_id
                else:
                    project_id = None
            else:
                project_id = None

                if not project_id:
                    # 3. Look for alphanumeric string (8-15 chars, usually letters + numbers)
                    # Like AV31000100
                    alpha_num = re.search(r'\b([A-Z0-9]{6,15})\b', text)
                    if alpha_num:
                        project_id = alpha_num.group(1)
                    else:
                        # 4. Last resort: Find any 3-6 digit number that ISN'T a year (2024-2027)
                        numbers = re.findall(r'\b(\d{3,6})\b', text)
                        for num in numbers:
                            if not (2020 <= int(num) <= 2030):
                                project_id = num
                                break
                    
                if not project_id:
                    # STABLE FALLBACK: Hash the title only, which is less likely to change than the full row text
                    import hashlib
                    clean_title = "".join(filter(str.isalnum, title)).lower()
                    project_id = f"_{hashlib.md5(clean_title.encode()).hexdigest()[:8]}"
            
            # Construct URL if extraction failed or returned dummy '#'
            if (not url or url == "#" or "javascript" in url) and not project_id.startswith("_"):
                # Construct standard OpenGov project URL
                url = f"https://procurement.opengov.com/portal/{portal_key}/projects/{project_id}"
            
            # Extract Release Date
            # Common formats: "Feb 3, 2026", "February 3, 2026", "Mar 12, 2024"
            release_date = None
            date_match = re.search(r'([A-Z][a-z]+ \d{1,2}, \d{4})', text)
            if date_match:
                try:
                    date_str = date_match.group(1)
                    release_date = datetime.strptime(date_str, "%b %d, %Y")
                except ValueError:
                    try:
                        release_date = datetime.strptime(date_str, "%B %d, %Y")
                    except ValueError:
                        pass
            
            return Project(
                id=project_id,
                title=title[:200],
                portal=portal_key,
                url=url,
                release_date=release_date,
            )
        except Exception as e:
            return None
    
    def _extract_from_page_source(self, portal_key: str) -> List[Project]:
        """Fallback: extract project data from raw page source"""
        projects = []
        source = self.browser.get_page_source()
        
        # Look for JSON object patterns common in OpenGov
        # DEBUG: Print snippets to see what we're working with
            
        # Look for JSON object patterns common in OpenGov
        # Pattern 1: {"id":12345,"title":"..."} or {"id":12345,..."title":"..."}
        # We enforce strict proximity (e.g. within 600 chars) to ensure we don't cross object boundaries
        # We use . instead of [^}] because there might be nested objects (like "template":{...}) between title and id
        patterns = [
            # Title ... ID (Allows alphanumeric IDs with dashes/spaces)
            r'"title"\s*:\s*"([^"]+)".{0,600}?"id"\s*:\s*"([^"]+)"',
            # ID ... Title
            r'"id"\s*:\s*"([^"]+)".{0,600}?"title"\s*:\s*"([^"]+)"',
             # Alternative format with 'jobTitle'
            r'"id"\s*:\s*"([^"]+)".{0,600}?"jobTitle"\s*:\s*"([^"]+)"',
            # Numeric ID specific patterns (just in case)
            r'"id"\s*:\s*(\d+).{0,600}?"title"\s*:\s*"([^"]+)"',
        ]
        
        seen_ids = set()
        
        for pattern in patterns:
            matches = re.findall(pattern, source)
            for match in matches:
                # Handle tuple unpacking based on which group is which
                if pattern.startswith(r'"title"'):
                    title, pid = match
                else:
                    pid, title = match
                    
                if pid in seen_ids:
                    continue
                
                # Check for "department" ID (common false positive)
                # Look at the text immediately preceding the ID match in the source
                # If we see "department":{"id":, then it's a department, not a project
                start_index = source.find(f'"id":{pid}')
                if start_index == -1:
                    start_index = source.find(f'"id": {pid}')
                
                if start_index > 0:
                     preceding_text = source[max(0, start_index-20):start_index]
                     if '"department":{' in preceding_text or '"department": {' in preceding_text:
                         continue
                    
                # Basic validation
                if len(title) < 3 or len(pid) < 3:
                    continue
                    
                # Check if it looks like a project (has status)
                # This is a heuristic to avoid random other IDs
                if '"status":' not in source[source.find(pid):source.find(pid)+500]:
                     # If we can't verify it's a project, skip generic small IDs
                     if len(pid) < 4: continue

                seen_ids.add(pid)
                
                url = f"https://procurement.opengov.com/portal/{portal_key}/projects/{pid}"
                
                projects.append(Project(
                    id=pid,
                    title=title,
                    portal=portal_key,
                    url=url,
                    release_date=datetime.now(), # Fallback date
                ))
        
        return projects
