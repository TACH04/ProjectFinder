"""
Scraper for Glendale, AZ Vendor Portal
"""
import time
from datetime import datetime
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper

@register_scraper("glendale")
class GlendaleScraper(BaseScraper):
    """Scraper for Glendale AZ Vendor Portal"""
    
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from Glendale AZ portal
        
        Steps:
        1. Navigate to portal
        2. Ensure "Any type" is selected (default)
        3. Click "Open Bids only"
        4. Click Search
        5. Extract project data
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping (Glendale): {portal_name}")
        print(f"{'='*50}")
        
        # 1. Navigate
        if not self.browser.navigate(url):
            error_msg = f"Failed to load portal: {portal_name}"
            print(f"  ✗ {error_msg}")
            raise PortalScrapingError(error_msg)
            
        # 2. Select "Any type" (default, but good to ensure)
        # We can just skip this if it's default, or try to select it if needed.
        # Based on exploration, it seems to default to "Any Type".
        # Let's verify if the element exists.
        
        # 3. Force "Open Bids only" (JS to bypass focus issues)
        try:
            if self.browser.wait_for_element(By.ID, "OpenBidsOnly"):
                checkbox = self.browser.find_element(By.ID, "OpenBidsOnly")
                
                # Force check via JS
                self.browser.driver.execute_script("arguments[0].checked = true;", checkbox)
                print("  Forced 'Open Bids only' state via JS")
                
                # Verify state
                if not checkbox.is_selected():
                    print("  ⚠ JS check failed, attempting standard click...")
                    checkbox.click()
            else:
                print("  ⚠ 'Open Bids only' checkbox not found")
        except Exception as e:
            print(f"  ⚠ Error selecting Open Bids: {e}")

        # 4. Click Search and wait for results
        max_retries = 2
        search_successful = False
        
        for attempt in range(max_retries + 1):
            try:
                if attempt > 0:
                    print(f"  Retry attempt {attempt} for Search...")
                    
                # Find button again to avoid stale element
                search_btn = self.browser.find_element(By.ID, "ctl00_ctl00_PrimaryPlaceHolder_ContentPlaceHolderMain_Search")
                
                if search_btn:
                    # Scroll into view
                    self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", search_btn)
                    time.sleep(0.5)

                    print(f"  Clicking Search (attempt {attempt + 1})...")
                    try:
                        search_btn.click()
                    except Exception as click_err:
                        print(f"  ⚠ Standard click failed: {click_err}")
                        print("  Attempting JS click...")
                        self.browser.driver.execute_script("arguments[0].click();", search_btn)
                    
                    # Wait for table to appear (increased timeout to 20s)
                    print(f"  Waiting for results table...")
                    if self.browser.wait_for_element(By.ID, "ctl00_ctl00_PrimaryPlaceHolder_ContentPlaceHolderMain_MolGridView1", timeout=20):
                        search_successful = True
                        break
                    else:
                        print(f"  ⚠ Results table did not appear within 20s")
                else:
                    print(f"  ⚠ Search button not found")
            except Exception as e:
                print(f"  ⚠ Error interacting with Search: {e}")
            
            if attempt < max_retries:
                time.sleep(2) # Brief pause before retry
        
        if not search_successful:
            print("  ✗ Failed to load search results after retries")
            
            # Capture screenshot for debugging
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"logs/screenshots/glendale_error_{timestamp}.png"
            self.browser.save_screenshot(screenshot_path)
            
            return []

        # 5. Extract
        print("  Extracting projects...")
        projects = self._extract_projects(portal_key)
        
        print(f"  ✓ Found {len(projects)} active projects")
        return projects

    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Extract projects from the table"""
        projects = []
        
        try:
            # Table selector
            table = self.browser.find_element(By.ID, "ctl00_ctl00_PrimaryPlaceHolder_ContentPlaceHolderMain_MolGridView1")
            
            # Rows (skip header)
            # The header is usually the first row.
            rows = table.find_elements(By.TAG_NAME, "tr")
            
            # Skip the first row (header)
            if len(rows) > 0:
                rows = rows[1:]
                
            print(f"    Found {len(rows)} data rows")
            
            for row in rows:
                project = self._parse_row(row, portal_key)
                if project:
                    projects.append(project)
                    
        except Exception as e:
            print(f"    ⚠ Error extracting projects: {e}")
            
        return projects

    def _parse_row(self, row, portal_key: str) -> Optional[Project]:
        """Parse a single row"""
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) < 4:
                return None
                
            # Column 2: Bid Number (and Link)
            # Column 3: Description / Title
            # Column 4: Closing Date / Due Date
            
            id_cell = cells[1]
            title_cell = cells[2]
            date_cell = cells[3]
            
            # Extract ID and URL
            project_id = id_cell.text.strip()
            url = None
            try:
                link = id_cell.find_element(By.TAG_NAME, "a")
                href = link.get_attribute("href")
                if href and "javascript" not in href:
                    url = href
            except NoSuchElementException:
                pass
            
            # Extract Title
            title = title_cell.text.strip()
            
            # Extract Date
            release_date = None
            date_text = date_cell.text.strip()
            
            if date_text:
                try:
                    # Try M/D/y H:M:S first (2-digit year)
                    # Example: '02/23/26 02:00 PM'
                    release_date = datetime.strptime(date_text, "%m/%d/%y %I:%M %p")
                except ValueError:
                    try:
                        # Try M/D/Y (4-digit year) just in case
                        release_date = datetime.strptime(date_text, "%m/%d/%Y %I:%M %p")
                    except ValueError:
                         try:
                            # Try M/D/Y or M/D/y without time
                            release_date = datetime.strptime(date_text, "%m/%d/%y")
                         except ValueError:
                             pass

            return Project(
                id=project_id,
                title=title,
                portal=portal_key,
                url=url or "https://glendaleazvendors.munisselfservice.com/Vendors/VBids/Default.aspx", 
                release_date=release_date or datetime.now()
            )

        except Exception as e:
            # print(f"Row parse error: {e}")
            return None
