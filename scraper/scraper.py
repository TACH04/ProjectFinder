"""
Core scraping logic for OpenGov Procurement portals
"""

import time
import re
from datetime import datetime, date
from dataclasses import dataclass
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from scraper.browser import StealthBrowser


@dataclass
class Project:
    """Represents a procurement project - simplified to only track essential data"""
    id: str
    title: str
    portal: str  # Portal key (e.g., 'phoenix', 'surpriseaz')

    url: Optional[str] = None
    release_date: Optional[datetime] = None
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "portal": self.portal,
            "url": self.url,
            "release_date": self.release_date.isoformat() if self.release_date else None,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        # Handle old data format that may have extra fields
        release_date = None
        if data.get("release_date"):
            try:
                release_date = datetime.fromisoformat(data["release_date"])
            except ValueError:
                pass
                
        return cls(
            id=data["id"],
            title=data["title"],
            portal=data["portal"],
            url=data.get("url"),
            release_date=release_date,
        )



class PortalScrapingError(Exception):
    """Raised when scraping a portal fails (e.g. timeout, Cloudflare block)"""
    pass


class OpenGovScraper:
    """Scraper for OpenGov Procurement portals"""
    
    def __init__(self, browser: StealthBrowser):
        self.browser = browser
        
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from a portal
        
        Steps:
        1. Navigate to portal
        2. Click "Active" status filter
        3. Double-click "Release Date" to sort newest first
        4. Click Search
        5. Extract project data
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
        
        # Step 2: Sort by Release Date (newest first = double click)
        print("  Step 2: Sorting by Release Date (newest first)...")
        if not self._sort_by_release_date():
            print("  ⚠ Could not sort by release date, continuing anyway...")
        
        # Step 3: Click Search button
        print("  Step 3: Triggering search...")
        if not self._click_search():
            print("  ⚠ Could not click search, continuing anyway...")
        
        # Wait for results to load - wait for rows to be present
        # self.browser.wait_for_element(By.XPATH, "//div[@role='row']|//tr") 
        # Actually, since we might have just sorted/searched, we should probably wait for stale or just a short delay
        # But let's trust that _extract_projects will wait or retry if needed
        time.sleep(1) # Short sleep to allow UI update
        
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
                        time.sleep(1)
                        return True
            except Exception as e:
                print(f"    ⚠ Error checking selector {selector}: {e}")
                continue
        
        return False
    
    def _sort_by_release_date(self) -> bool:
        """Double-click Release Date header to sort descending"""
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
                # print(f"    Checking selector: {selector}")
                elements = self.browser.find_elements(By.XPATH, selector)
                
                # Filter for visible elements
                visible_elements = [e for e in elements if e.is_displayed()]
                
                if not visible_elements:
                    continue
                    
                target = visible_elements[0]
                print(f"      ✓ Found visible header")
                
                # Click 1
                try:
                    target.click()
                except Exception:
                    self.browser.driver.execute_script("arguments[0].click();", target)
                
                # Small delay between clicks for UI to register double click intent or sort change
                time.sleep(0.5) 
                
                # Re-find for Click 2
                # We re-find because the DOM might have updated slightly, or to be safe
                elements_retry = self.browser.find_elements(By.XPATH, selector)
                visible_elements_retry = [e for e in elements_retry if e.is_displayed()]
                
                if visible_elements_retry:
                    target = visible_elements_retry[0]
                    try:
                        target.click()
                    except Exception:
                         self.browser.driver.execute_script("arguments[0].click();", target)
                    print("      ✓ Sorted by release date (Double Clicked)")
                    return True
                
            except Exception as e:
                # print(f"    ⚠ Error on selector {selector}: {e}")
                continue
        
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
                        time.sleep(1)
                        return True
            except Exception:
                continue
        
        return False
    
    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Extract project data from the results table/list"""
        projects = []
        
        # Try to find project rows in various table/list structures
        row_selectors = [
            "//tr[contains(@class, 'row')]",
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
            

            # Try to find a project ID (usually numeric or alphanumeric pattern)
            # 1. Look for labeled ID: "ID: 123", "#123", "Project #123"
            id_match = re.search(r'(?:ID|#|Project|Number)\s*:?\s*([A-Za-z0-9-]+)', text, re.IGNORECASE)
            
            if id_match:
                project_id = id_match.group(1)
            else:
                # 2. Look for formatted IDs (e.g., "IFB-25-001")
                formatted_id = re.search(r'\b([A-Z]{2,}-\d{2,}-[\w-]+)\b', text)
                if formatted_id:
                    project_id = formatted_id.group(1)
                else:
                    # 3. Last resort: Find any 3-6 digit number that ISN'T a year (2024-2027)
                    # We look for a number that is NOT 202x
                    numbers = re.findall(r'\b(\d{3,6})\b', text)
                    project_id = None
                    for num in numbers:
                        # Skip likely years
                        if not (2020 <= int(num) <= 2030):
                            project_id = num
                            break
                    
                    if not project_id:
                        project_id = f"_{hash(text) % 100000}"
            
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
        if "id" in source and "title" in source:
            print("  🔍 Debug: Found 'id' and 'title' in source. Check structure:")
            idx = source.find('"id"')
            if idx != -1:
                print(f"    Snippet around first 'id': {source[idx:idx+300]}")
            
        # Look for JSON object patterns common in OpenGov
        # Pattern 1: {"id":12345,"title":"..."} or {"id":12345,..."title":"..."}
        # We enforce strict proximity (e.g. within 600 chars) to ensure we don't cross object boundaries
        # We use . instead of [^}] because there might be nested objects (like "template":{...}) between title and id
        patterns = [
            # Title ... ID (Most common based on debug output)
            r'"title"\s*:\s*"([^"]+)".{0,600}?"id"\s*:\s*(\d+)',
            # ID ... Title
            r'"id"\s*:\s*(\d+).{0,600}?"title"\s*:\s*"([^"]+)"',
             # Alternative format with 'jobTitle'
            r'"id"\s*:\s*(\d+).{0,600}?"jobTitle"\s*:\s*"([^"]+)"',
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
