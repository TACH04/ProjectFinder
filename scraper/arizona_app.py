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
        row_selector = "tr[id^='body_x_grid_grd_tr_']"
        
        try:
            if not self.browser.wait_for_element(By.CSS_SELECTOR, row_selector, timeout=30):
                source = self.browser.get_page_source().lower()
                if "no records found" in source or "no results" in source:
                    print("  ✓ No active projects found.")
                    return []
                print("  ⚠ Timed out waiting for table rows.")
        except Exception as e:
            print(f"  ⚠ Error waiting for elements: {e}")

        # Step 1: Ensure sorting by Begin Date Descending
        print("  Ensuring records are sorted by 'Begin Date' descending...")
        self._ensure_descending_sort()

        # Step 2: Pagination Loop
        all_projects = []
        page_count = 0
        max_pages = 20 # Safety limit
        
        # Calculate 30-day cutoff
        from datetime import timedelta
        cutoff_date = datetime.now() - timedelta(days=30)
        reached_cutoff = False

        while page_count < max_pages and not reached_cutoff:
            page_count += 1
            print(f"  Scraping page {page_count}...")
            
            # Get current first row ID to detect page change later
            first_row_id = self._get_first_row_id()
            
            # Extract projects from current page
            page_projects = self._extract_projects(portal_key)
            
            # Check for projects older than cutoff
            current_page_valid = []
            for p in page_projects:
                if p.release_date and p.release_date < cutoff_date:
                    print(f"    - Found project {p.id} from {p.release_date.strftime('%Y-%m-%d')} (before cutoff). Stopping.")
                    reached_cutoff = True
                    # We can stop here because they are sorted descending
                    break
                current_page_valid.append(p)
            
            all_projects.extend(current_page_valid)
            
            if reached_cutoff or not self._has_next_page():
                break
                
            # Click next and wait
            print("    Moving to next page...")
            if not self._click_next_page(first_row_id):
                break

        print(f"  ✓ Found {len(all_projects)} projects from the last 30 days.")
        return all_projects

    def _ensure_descending_sort(self):
        """Sort the grid by Begin Date (Column 10/Index 7 in headers) descending."""
        try:
            # Headers have IDs like body_x_grid_grd__ctl0_colBeginDate
            begin_header = None
            headers = self.browser.find_elements(By.TAG_NAME, "th")
            for h in headers:
                if "Begin (UTC-7)" in h.text:
                    begin_header = h
                    break
            
            if not begin_header:
                print("    ⚠ Could not find 'Begin (UTC-7)' date header for sorting.")
                return

            # Check sort state from the icon class inside the sort button
            # Icons: fa-sort (none), fa-sort-up (asc), fa-sort-down (desc)
            for attempt in range(3): # Max 2 clicks needed from any state
                sort_btn = None
                icon_class = ""
                try:
                    sort_btn = begin_header.find_element(By.CSS_SELECTOR, "button, a")
                    icon = sort_btn.find_element(By.TAG_NAME, "i")
                    icon_class = icon.get_attribute("class") or ""
                except Exception:
                    pass

                print(f"    Current sort icon class: '{icon_class}'")
                
                if "fa-sort-down" in icon_class:
                    print("    ✓ Confirmed descending sort (via icon).")
                    return
                
                print("    Clicking 'Begin' sort button to change sort order...")
                if sort_btn:
                    sort_btn.click()
                else:
                    begin_header.click()
                
                time.sleep(5) # Wait for AJAX sort
                
                # Re-fetch everything
                headers = self.browser.find_elements(By.TAG_NAME, "th")
                for h in headers:
                    if "Begin (UTC-7)" in h.text:
                        begin_header = h
                        break
        except Exception as e:
            print(f"    ⚠ Error during sorting: {e}")

    def _get_first_row_id(self) -> Optional[str]:
        """Get the ID of the first project row in the grid."""
        try:
            first_row = self.browser.find_element(By.CSS_SELECTOR, "tr[id^='body_x_grid_grd_tr_']")
            return first_row.get_attribute("id")
        except Exception:
            return None

    def _has_next_page(self) -> bool:
        """Check if there is a next page button and it's not disabled."""
        try:
            next_btn = self.browser.find_element(By.CSS_SELECTOR, "button#body_x_grid_gridPagerBtnNextPage")
            classes = next_btn.get_attribute("class") or ""
            return "disabled" not in classes.lower()
        except Exception:
            return False

    def _click_next_page(self, prev_first_row_id: Optional[str]) -> bool:
        """Click the next page button and wait for the grid to update."""
        try:
            next_btn = self.browser.find_element(By.CSS_SELECTOR, "button#body_x_grid_gridPagerBtnNextPage")
            next_btn.click()
            
            # Wait for content to change - either rows disappear/reappear or first row ID changes
            start_time = time.time()
            while time.time() - start_time < 20:
                current_id = self._get_first_row_id()
                if current_id and current_id != prev_first_row_id:
                    time.sleep(1) # Let it settle
                    return True
                time.sleep(0.5)
            
            print("    ⚠ Timeout waiting for next page to load.")
            return False
        except Exception as e:
            print(f"    ⚠ Error clicking next page: {e}")
            return False

    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Extract project data from the current results table"""
        projects = []
        
        try:
            # Selector for all rows in the results grid
            rows = self.browser.find_elements(By.CSS_SELECTOR, "tr[id^='body_x_grid_grd_tr_']")
            print(f"    Found {len(rows)} rows on page.")
            
            for i, row in enumerate(rows):
                project = self._parse_project_row(row, portal_key)
                if project:
                    if i < 3:
                        print(f"      [{i+1}] {project.id}: {project.release_date.strftime('%Y-%m-%d') if project.release_date else 'N/A'}")
                    projects.append(project)
        except Exception as e:
            print(f"    ⚠ Error during row extraction: {e}")
            
        return projects

    def _parse_project_row(self, row, portal_key: str) -> Optional[Project]:
        """Parse a single Arizona APP project row"""
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) < 11:
                return None
                
            row_id = row.get_attribute("id")
            internal_id = row_id.split("_")[-1] if row_id else None
            
            # Content extraction (Mapping confirmed via research)
            # Index 1: Code
            code = cells[1].text.strip()
            # Index 2: Label
            title = cells[2].text.strip()
            # Index 10: Begin (UTC-7)
            date_str = cells[10].text.strip()
            
            # Detail URL
            detail_url = f"https://app.az.gov/page.aspx/en/bpm/process_manage_extranet/{internal_id}" if internal_id else None
            
            # Parse Date
            release_date = None
            if date_str:
                try:
                    clean_date_str = re.sub(r'\s*\([^)]*\)', '', date_str).strip()
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
