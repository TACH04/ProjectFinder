"""
Scraper for PlanetBids Procurement portals
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


@register_scraper("planetbids")
class PlanetBidsScraper(BaseScraper):
    """Scraper for PlanetBids Procurement portals"""
    
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from a PlanetBids portal.
        
        Steps:
        1. Navigate to portal search page
        2. Wait for the bid table to load
        3. Extract project data from table rows
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping (PlanetBids): {portal_name}")
        print(f"{'='*50}")
        
        # Navigate to portal
        if not self.browser.navigate(url):
            error_msg = f"Failed to load portal: {portal_name}"
            print(f"  ✗ {error_msg}")
            raise PortalScrapingError(error_msg)
        
        # Wait for the table rows to appear
        print("  Waiting for bid results...")
        # PlanetBids uses role="row" for the table rows
        if not self.browser.wait_for_element(By.CSS_SELECTOR, "tr[role='row']", timeout=20):
            # Check if there's a "No records found" message
            source = self.browser.get_page_source().lower()
            if "no records found" in source or "no results" in source:
                print("  ✓ No active projects found.")
                return []
            
            print("  ⚠ Timed out waiting for bid results to load")
            # We'll try to extract anyway, maybe it's just slow
        
        # Extract projects
        print("  Extracting projects...")
        projects = self._extract_projects(portal_key, url)
        
        print(f"  ✓ Found {len(projects)} active projects")
        return projects

    def _extract_projects(self, portal_key: str, portal_url: str) -> List[Project]:
        """Extract project data from the results table"""
        projects = []
        
        # Get portal ID from URL to construct detail URLs
        # Example: https://vendors.planetbids.com/portal/46991/bo/bo-search
        portal_id_match = re.search(r'/portal/(\d+)/', portal_url)
        portal_id = portal_id_match.group(1) if portal_id_match else "46991"
        
        try:
            rows = self.browser.find_elements(By.CSS_SELECTOR, "tr[role='row']")
            for row in rows:
                project = self._parse_project_row(row, portal_key, portal_id)
                if project:
                    projects.append(project)
        except Exception as e:
            print(f"    ⚠ Error during row extraction: {e}")
            
        return projects

    def _parse_project_row(self, row, portal_key: str, portal_id: str) -> Optional[Project]:
        """Parse a single PlanetBids project row"""
        try:
            # Columns in PlanetBids table:
            # 1: Posted Date
            # 2: Title
            # 3: Invitation #
            # 4: Due Date
            # 5: ...
            
            # The 'rowattribute' attribute on the <tr> contains the internal project ID
            internal_id = row.get_attribute("rowattribute")
            if not internal_id:
                return None
                
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) < 3:
                return None
                
            posted_date_str = cells[0].text.strip()
            title = cells[1].text.strip()
            invitation_num = cells[2].text.strip()
            
            # Construct Detail URL
            # Format: https://vendors.planetbids.com/portal/46991/bo/bo-detail/{internal_id}
            detail_url = f"https://vendors.planetbids.com/portal/{portal_id}/bo/bo-detail/{internal_id}"
            
            # Use invitation_num as part of ID with portal prefix for uniqueness
            project_id = f"{invitation_num}" if invitation_num else f"PB-{internal_id}"
            
            # Parse Date - PlanetBids usually uses MM/DD/YYYY or similar
            release_date = None
            if posted_date_str:
                try:
                    # Try common formats
                    for fmt in ["%m/%d/%Y", "%b %p, %Y", "%B %d, %Y"]:
                        try:
                            release_date = datetime.strptime(posted_date_str, fmt)
                            break
                        except ValueError:
                            continue
                except Exception:
                    pass

            return Project(
                id=project_id,
                title=title,
                portal=portal_key,
                url=detail_url,
                release_date=release_date or datetime.now()
            )
            
        except Exception as e:
            # print(f"    ⚠ Error parsing row: {e}")
            return None
