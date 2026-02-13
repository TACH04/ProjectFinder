"""
Scraper for City of Cave Creek, AZ
"""
import re
import time
from datetime import datetime
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper

@register_scraper("cave_creek")
class CaveCreekScraper(BaseScraper):
    """Scraper for City of Cave Creek, AZ"""
    
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
            
        # Wait for either row items OR "No records" message
        try:
            # Wait for listItemsRow, or catHeader (table container), or "No postings" text
            # Wait for listItemsRow or "No postings" text
            # The "catHeader" ID does not exist.
            WebDriverWait(self.browser.driver, 10).until(
                lambda d: d.find_elements(By.CSS_SELECTOR, "div.listItemsRow.bid") or \
                          "There are no open bid postings" in d.page_source or \
                          "No postings" in d.page_source
            )
        except Exception:
            print("  ⚠ Timed out waiting for content (might be empty)")

        projects = []
        
        # Select all bid rows
        rows = self.browser.find_elements(By.CSS_SELECTOR, "div.listItemsRow.bid")
        
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
        """Parse a single bid row"""
        try:
            # 1. Title and Link
            # Structure: <div class="bidTitle"><span><a href="...">Title</a></span>...</div>
            title_elem = row.find_element(By.CSS_SELECTOR, "div.bidTitle a")
            title = title_elem.text.strip()
            url = title_elem.get_attribute("href")
            
            # 2. Project ID extraction
            # Structure: <div class="bidTitle">... <span id="..."><strong>Bid No.</strong> 2024-01</span> ...</div>
            # We get all text from the title container to be safe
            title_container = row.find_element(By.CSS_SELECTOR, "div.bidTitle")
            full_text = title_container.text
            
            # Default ID fallback
            project_id = f"cc_{abs(hash(title))}" 
            
            # Look for "Bid No." pattern: "Bid No. 2024-05" 
            # Note: The browser analysis showed "Bid No." inside a strong tag
            id_match = re.search(r'Bid No\.?\s*([A-Za-z0-9-]+)', full_text, re.IGNORECASE)
            if id_match:
                project_id = id_match.group(1)
            
            # 3. Dates/Status
            # Structure: <div class="bidStatus">...<div>Open<br>March 1, 2025...</div></div>
            release_date = None
            
            try:
                status_container = row.find_element(By.CSS_SELECTOR, "div.bidStatus")
                # Get the text from the second column (values column)
                # It usually contains "Status" then "Closing Date"
                status_text = status_container.text
                
                # Parse date - usually "Month DD, YYYY"
                # Ex: "March 6, 2025 2:00 PM"
                # We prioritize the closing date since release date isn't always clear
                date_match = re.search(r'([A-Z][a-z]+ \d{1,2}, \d{4})', status_text)
                if date_match:
                    date_str = date_match.group(1)
                    release_date = datetime.strptime(date_str, "%B %d, %Y")
                
            except Exception:
                pass 

            # If no date found, use today
            if not release_date:
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
