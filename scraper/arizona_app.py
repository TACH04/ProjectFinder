"""
Scraper for Arizona Procurement Portal (APP)
"""

import time
import re
from datetime import datetime
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper


@register_scraper("arizona_app")
class ArizonaAPPScraper(BaseScraper):
    """Scraper for Arizona Procurement Portal (APP)"""
    requires_browser = True
    
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from the Arizona Procurement Portal.
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping (Arizona APP): {portal_name}")
        print(f"{'='*50}")
        
        # Navigate to portal
        if not self.browser.navigate(url):
            error_msg = f"Failed to load portal: {portal_name}"
            print(f"  ✗ {error_msg}")
            raise PortalScrapingError(error_msg)
        
        # Wait for the table rows to appear
        print("  Waiting for RFP results table...")
        # Based on DOM analysis: tr[id^='body_x_grid_grd_tr_']
        row_selector = "tr[id^='body_x_grid_grd_tr_']"
        
        try:
            # First wait for the table itself if possible, or just the rows
            if not self.browser.wait_for_element(By.CSS_SELECTOR, row_selector, timeout=30):
                # Check for "no records"
                source = self.browser.get_page_source().lower()
                if "no records found" in source or "no results" in source:
                    print("  ✓ No active projects found.")
                    return []
                print("  ⚠ Timed out waiting for table rows.")
        except Exception as e:
            print(f"  ⚠ Error waiting for elements: {e}")

        # Extract projects
        print("  Extracting projects...")
        projects = self._extract_projects(portal_key)
        
        print(f"  ✓ Found {len(projects)} active projects")
        return projects

    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Extract project data from the results table"""
        projects = []
        
        try:
            # Selector for all rows in the results grid
            rows = self.browser.find_elements(By.CSS_SELECTOR, "tr[id^='body_x_grid_grd_tr_']")
            for row in rows:
                project = self._parse_project_row(row, portal_key)
                if project:
                    projects.append(project)
        except Exception as e:
            print(f"    ⚠ Error during row extraction: {e}")
            
        return projects

    def _parse_project_row(self, row, portal_key: str) -> Optional[Project]:
        """Parse a single Arizona APP project row"""
        try:
            # Columns based on nth-child analysis (handles hidden columns):
            # td:nth-child(1) -> Link (Pencil icon)
            # td:nth-child(2) -> Code
            # td:nth-child(3) -> Label
            # td:nth-child(6) -> Agency
            # td:nth-child(11) -> Begin Date
            
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) < 11: # Ensure we have enough columns
                return None
                
            # Internal ID extraction from row ID: body_x_grid_grd_tr_13557
            row_id = row.get_attribute("id")
            internal_id = row_id.split("_")[-1] if row_id else None
            
            # Content extraction
            # Code is in index 1 (nth-child 2)
            code = cells[1].text.strip()
            # Label is in index 2 (nth-child 3)
            title = cells[2].text.strip()
            # Begin date is in index 10 (nth-child 11)
            date_str = cells[10].text.strip()
            
            # Construct Detail URL
            # Pattern: https://app.az.gov/page.aspx/en/bpm/process_manage_extranet/[INTERNAL_ID]
            detail_url = f"https://app.az.gov/page.aspx/en/bpm/process_manage_extranet/{internal_id}" if internal_id else None
            
            # Parse Date
            # Format expected: M/d/yyyy (from screenshot notice)
            # Actual text might include time: "4/7/2026 5:00:00 PM"
            release_date = None
            if date_str:
                try:
                    # Strip any " (UTC-7)" etc if present in text (though screenshot shows it in header)
                    clean_date_str = re.sub(r'\s*\([^)]*\)', '', date_str).strip()
                    # Common format: "4/7/2026 5:00:00 PM"
                    date_formats = ["%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y", "%n/%j/%Y %I:%M:%S %p"]
                    for fmt in date_formats:
                        try:
                            release_date = datetime.strptime(clean_date_str, fmt)
                            break
                        except ValueError:
                            continue
                except Exception:
                    pass

            return Project(
                id=code or f"AZ-{internal_id}",
                title=title,
                portal=portal_key,
                url=detail_url,
                release_date=release_date or datetime.now()
            )
            
        except Exception:
            return None
