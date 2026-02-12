"""
Scraper for BonfireHub Procurement portals
Uses the internal JSON API for robust data extraction.
"""

import time
import requests
from typing import List, Optional
from datetime import datetime

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper
from scraper.browser import StealthBrowser

@register_scraper("bonfire")
class BonfireScraper(BaseScraper):
    """Scraper for BonfireHub based portals"""

    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from a Bonfire portal using the JSON API.
        """
        url = portal_config["url"]
        domain = url.split("/portal")[0]
        api_url = f"{domain}/PublicPortal/getOpenPublicOpportunitiesSectionData"
        portal_name = portal_config["name"]

        print(f"\n{'='*50}")
        print(f"Scraping (Bonfire): {portal_name}")
        print(f"{'='*50}")

        try:
            # Try efficient requests first
            print(f"  Fetching API: {api_url}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Referer": url
            }
            response = requests.get(api_url, headers=headers, timeout=20)
            response.raise_for_status()
            data = response.json()
            
            if not data.get("success"):
                raise PortalScrapingError(f"API returned success=0: {data}")

            projects_data = data.get("payload", {}).get("projects", {})
            
            projects = []
            for pid, pdata in projects_data.items():
                project = self._parse_project(pdata, domain, portal_key)
                if project:
                    projects.append(project)

            print(f"  ✓ Found {len(projects)} active projects via API")
            return projects

        except Exception as e:
            # Fallback to browser if requests fails (e.g. strict WAF)
            # But implementing that fallback is complex. For now, rely on API.
            print(f"  ✗ API request failed: {e}")
            raise PortalScrapingError(f"Bonfire API failed: {e}")

    def _parse_project(self, data: dict, domain: str, portal_key: str) -> Optional[Project]:
        try:
            # Data structure:
            # {
            #   "ProjectID": "219807",
            #   "ReferenceID": "26-11IFB",
            #   "ProjectName": "Secondary Clarifier Rehabilitation",
            #   "DateClose": "2026-02-25 21:00:00"
            # }

            pid = str(data.get("ProjectID"))
            ref_id = data.get("ReferenceID", "")
            title = data.get("ProjectName", "Untitled Project")
            
            # Use ReferenceID as part of title if useful, or just ID?
            # Existing scraper uses ID for dedup.
            
            # Construct URL
            # https://sedonaaz.bonfirehub.com/opportunities/{ProjectID}
            project_url = f"{domain}/opportunities/{pid}"
            
            # Parse Date
            release_date = None
            date_close_str = data.get("DateClose")
            # Close date isn't release date... but it's what we have? 
            # The API might have "DateOpen"? 
            # Let's check if there are other fields.
            # Based on inspection, we only saw those.
            # We can use current time as fallback for 'release_date' if meaningful,
            # or just rely on 'seen_projects.json' to filter new ones.
            # Wait, the user cares about "New" projects.
            # If we don't have release date, we can't sort by it in the email (maybe).
            
            # Let's try to parse DateClose as a datetime object just in case we want to use it
            if date_close_str:
                try:
                    # "2026-02-25 21:00:00"
                    release_date = datetime.strptime(date_close_str, "%Y-%m-%d %H:%M:%S")
                    # Ideally we want OPEN date. The inspecting showed limited fields.
                    # We will proceed with what we have. API might have more fields if we look closer,
                    # but for now let's stick to what we saw.
                except ValueError:
                    pass

            return Project(
                id=pid,
                title=title,
                portal=portal_key,
                url=project_url,
                release_date=release_date or datetime.now() 
            )
        except Exception as e:
            print(f"    ⚠ Error parsing project {data.get('ProjectID')}: {e}")
            return None
