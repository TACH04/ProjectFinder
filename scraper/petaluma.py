"""
Scraper for City of Petaluma Bid Opportunities
"""
import hashlib
from datetime import datetime
from typing import List, Optional

from selenium.webdriver.common.by import By
from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper

@register_scraper("petaluma")
class PetalumaScraper(BaseScraper):
    """Scraper for City of Petaluma bid opportunities portal"""
    
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from Petaluma portal.
        Extracts all projects directly from the main listing page to save time.
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping (Petaluma): {portal_name}")
        print(f"{'='*50}")
        
        # 1. Navigate to main page
        if not self.browser.navigate(url):
            error_msg = f"Failed to load portal: {portal_name}"
            print(f"  ✗ {error_msg}")
            raise PortalScrapingError(error_msg)
            
        # 2. Extract projects
        print("  Extracting projects from main list...")
        projects = self._extract_projects(portal_key)
        
        print(f"  ✓ Finished Petaluma: {len(projects)} projects found")
        return projects

    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Find projects under the relevant section headers and return Project objects"""
        projects = []
        seen_urls = set()
        
        target_headers = [
            "CURRENT BID OPPORTUNITIES",
            "CURRENT REQUEST FOR PROPOSAL OPPORTUNITIES",
            "CURRENT REQUEST FOR QUALIFICATIONS OPPORTUNITIES"
        ]
        
        try:
            # Find all h2 headers
            headers = self.browser.find_elements(By.TAG_NAME, "h2")
            
            for header in headers:
                header_text = header.text.strip().upper()
                if any(target in header_text for target in target_headers):
                    # Found a target section. Now look for links in its parent panel.
                    try:
                        # Find the panel container
                        panel = header.find_element(By.XPATH, "./ancestor::div[contains(@class, 'so-panel')]")
                        links = panel.find_elements(By.TAG_NAME, "a")
                        
                        for link in links:
                            title = link.text.strip()
                            href = link.get_attribute("href")
                            
                            # Validation: skip empty links, external links, or duplicates
                            if not title or not href:
                                continue
                            if "cityofpetaluma.org" not in href or "#" in href:
                                continue
                            if href in seen_urls:
                                continue
                                
                            seen_urls.add(href)
                            
                            # Generate a stable ID from the URL
                            id_hash = hashlib.md5(href.encode()).hexdigest()[:8]
                            project_id = f"petaluma_{id_hash}"
                            
                            projects.append(Project(
                                id=project_id,
                                title=title,
                                portal=portal_key,
                                url=href,
                                release_date=datetime.now() # Use current time as fallback
                            ))
                            print(f"    + {title}")
                            
                    except Exception:
                        pass
                        
        except Exception as e:
            print(f"    ⚠ Error extracting projects: {e}")
            
        return projects
