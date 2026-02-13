"""
Scraper for City of Maricopa, AZ (eGovLink)
"""
import re
import time
from datetime import datetime
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper

@register_scraper("maricopa")
class MaricopaScraper(BaseScraper):
    """Scraper for City of Maricopa, AZ"""
    
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping: {portal_name}")
        print(f"{'='*50}")
        
        if not self.browser.navigate(url):
            error_msg = f"Failed to load portal: {portal_name}"
            print(f"  ✗ {error_msg}")
            raise PortalScrapingError(error_msg)
            
        try:
            # 1. Handle "Show expired postings" -> Set to "N"
            expired_select = WebDriverWait(self.browser.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "sc_show_expired"))
            )
            select = Select(expired_select)
            select.select_by_value("N")
            print("  ✓ Set 'Show expired postings' to 'No'")
            
            # 2. Click "Search" button
            search_btn = self.browser.driver.find_element(By.CSS_SELECTOR, 'input[name="sAction"][value="Search"]')
            search_btn.click()
            print("  ✓ Clicked 'Search'")
            
            # 3. Wait for results or "No records"
            # We wait for the results table or some indication of completion
            # The structure is table[bgcolor="#ffffff"] for results
            # We'll give it a moment to load
            time.sleep(2) 
            
        except Exception as e:
            print(f"  ⚠ Error interacting with form: {e}")
            return []

        projects = []
        
        # Select all result rows
        # Based on analysis: table[bgcolor="#ffffff"] containing a link to postings_info.asp
        # We find all tables with that bgcolor, then check if they contain the link
        potential_rows = self.browser.find_elements(By.CSS_SELECTOR, 'table[bgcolor="#ffffff"]')
        
        # Filter for actual posting rows (must have the link)
        rows = [
            row for row in potential_rows 
            if row.find_elements(By.CSS_SELECTOR, 'a[href*="postings_info.asp"]')
        ]
        
        if not rows:
             print("  ✓ No active projects found")
             return []

        print(f"  Found {len(rows)} potential project rows")
        
        for row in rows:
            try:
                # Basic validation - ensure row is displayed
                if not row.is_displayed():
                    continue
                    
                project = self._parse_project_row(row, portal_key)
                if project:
                    projects.append(project)
            except Exception as e:
                print(f"  ⚠ Error parsing row: {e}")
                continue
                
        print(f"  ✓ Found {len(projects)} active projects")
        return projects

    def _parse_project_row(self, row, portal_key: str) -> Optional[Project]:
        """Parse a single posting row"""
        try:
            # 1. Title and Link
            # Structure: <a href="postings_info.asp?posting_id=...">Title</a>
            title_elem = row.find_element(By.CSS_SELECTOR, 'a[href*="postings_info.asp"]')
            title = title_elem.text.strip()
            url = title_elem.get_attribute("href")
            
            # 2. Project ID extraction
            # URL is like: .../postings_info.asp?posting_id=1234
            # We can extract the ID from the URL
            project_id = f"mari_{abs(hash(title))}" # Fallback
            
            id_match = re.search(r'posting_id=(\d+)', url)
            if id_match:
                project_id = id_match.group(1)
            
            # 3. Dates
            # Structure: explicit "Closed:" text in the last column usually
            # We'll grab all text and look for the pattern if strict selector fails
            row_text = row.text
            
            release_date = None
            
            # Look for "Closed: MM/DD/YYYY" or similar
            # Based on subagent, it's in the last td
            
            # Try to find a date pattern in the whole row text
            # Matches: 1/15/2026, 01/15/2026, Jan 15, 2026
            date_match = re.search(r'Closed:\s*(\d{1,2}/\d{1,2}/\d{4})', row_text, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(1)
                try:
                    release_date = datetime.strptime(date_str, "%m/%d/%Y")
                except ValueError:
                    pass
            
            if not release_date:
                # Try finding just a date if "Closed:" prefix isn't there or different format
                # This is risky, but better than nothing if specific text is missing
                # For now, default to now if not found
                release_date = datetime.now()

            return Project(
                id=project_id,
                title=title,
                portal=portal_key,
                url=url,
                release_date=release_date 
            )
            
        except Exception as e:
            # print(f"Error detail: {e}")
            return None
