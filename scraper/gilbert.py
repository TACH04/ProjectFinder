"""
Scraper for Gilbert, AZ Purchasing Portal
"""

import time
import re
from datetime import datetime
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper
from scraper.browser import StealthBrowser

@register_scraper("gilbert")
class GilbertScraper(BaseScraper):
    """Scraper for Gilbert, AZ purchasing portal"""
    requires_browser = True
    
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from Gilbert AZ portal
        
        Steps:
        1. Navigate to portal
        2. Double-click "Closing" header to sort
        3. Extract project data
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping (Gilbert): {portal_name}")
        print(f"{'='*50}")
        
        # 1. Navigate
        if not self.browser.navigate(url):
            error_msg = f"Failed to load portal: {portal_name}"
            print(f"  ✗ {error_msg}")
            raise PortalScrapingError(error_msg)
            
        # Wait for table
        if not self.browser.wait_for_element(By.CSS_SELECTOR, "table tbody tr"):
             print("  ⚠ Timed out waiting for table, might be empty")
             
        # 2. Sort by Closing (Skipped - URL handles this)
        # print("  Step 2: Sorting by Closing Date (double click)...")
        # if not self._sort_by_closing():
        #     print("  ⚠ Could not sort by closing date, continuing...")
            
        # 3. Extract
        print("  Step 3: Extracting projects...")
        projects = self._extract_projects(portal_key)
        
        print(f"  ✓ Found {len(projects)} active projects")
        return projects

    def _sort_by_closing(self) -> bool:
        """Double click the sorting header"""
        # Selector identified: a[id^="RFPClosing_"]
        try:
            # Find the header
            headers = self.browser.find_elements(By.CSS_SELECTOR, "a[id^='RFPClosing_']")
            visible_headers = [h for h in headers if h.is_displayed()]
            
            if not visible_headers:
                print("    ✗ Could not find Closing header")
                return False
                
            header = visible_headers[0]
            
            # Click 1 - Use JS to avoid interception
            self.browser.driver.execute_script("arguments[0].click();", header)
            time.sleep(1.5) # Wait for reload
            
            print("    ✓ Sorted (Single Click)")
            return True
                
        except Exception as e:
            print(f"    ⚠ Error sorting: {e}")
            
        return False

    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Extract projects from the table"""
        projects = []
        
        try:
            rows = self.browser.find_elements(By.CSS_SELECTOR, "table tbody tr")
            print(f"    Found {len(rows)} rows")
            
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
            # Title & Link: td[data-th="Title"] a
            try:
                title_cell = row.find_element(By.CSS_SELECTOR, "td[data-th='Title']")
                link_elem = title_cell.find_element(By.TAG_NAME, "a")
                title = link_elem.text.strip()
                url = link_elem.get_attribute("href")
            except Exception:
                return None # Skip if no title/link
                
            # ID: td[data-th="RFP Number"]
            try:
                id_cell = row.find_element(By.CSS_SELECTOR, "td[data-th='RFP Number']")
                project_id = id_cell.text.strip()
            except Exception:
                project_id = f"gilbert_{int(time.time()*1000)}" # Fallback
                
            # Date: td[data-th="Closing"]
            release_date = None
            try:
                date_cell = row.find_element(By.CSS_SELECTOR, "td[data-th='Closing']")
                date_str = date_cell.text.strip()
                # Format: 03/11/2026 2:00 PM
                try:
                    release_date = datetime.strptime(date_str, "%m/%d/%Y %I:%M %p")
                except ValueError:
                    pass
            except Exception:
                pass
            
            # Status: td[data-th="Status"]
            try:
                status_cell = row.find_element(By.CSS_SELECTOR, "td[data-th='Status']")
                status = status_cell.text.strip().lower()
                if "closed" in status:
                    return None
            except Exception:
                pass

            return Project(
                id=project_id,
                title=title,
                portal=portal_key,
                url=url,
                release_date=release_date or datetime.now()
            )

        except Exception as e:
            # print(f"Row parse error: {e}")
            return None
