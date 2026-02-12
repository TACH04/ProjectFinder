"""
Scraper for City of Chandler, AZ Procurement portals
Parses static HTML content using BeautifulSoup
"""

import re
import requests
from datetime import datetime
from typing import List, Optional
from bs4 import BeautifulSoup

from scraper.scraper import Project, PortalScrapingError

class ChandlerScraper:
    """Scraper for Chandler AZ styled portals (RFQ and RFB/RFP)"""

    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from Chandler AZ pages.
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping (Chandler): {portal_name}")
        print(f"{'='*50}")

        try:
            print(f"  Fetching URL: {url}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            projects = []
            
            # The structure relies on accordion sections
            # We look for the main content area first
            content_area = soup.find('div', class_='region-content')
            if not content_area:
                print("  ⚠ Could not find main content area")
                return []

            # Find all accordion items
            # RFQ and RFB pages use similar structure:
            # <div class="card panel panel-default">
            #   <div class="card-header panel-heading" id="...">
            #     <div class="panel-title">
            #       <a ...> Project Title </a>
            
            # The projects are flattened inside a single "card panel panel-default" container
            # or sometimes multiple containers.
            # Best approach: Find ALL card-header elements, then find their associated bodies.
            
            project_headers = content_area.find_all('div', class_='card-header')
            if not project_headers:
                 project_headers = content_area.find_all('div', class_='panel-heading')
            
            print(f"  Found {len(project_headers)} (header) items")
            
            for header in project_headers:
                project = self._parse_project_header(header, portal_key, url)
                if project:
                    projects.append(project)

            print(f"  ✓ Found {len(projects)} active projects")
            return projects

        except Exception as e:
            print(f"  ✗ Scraping failed: {e}")
            raise PortalScrapingError(f"Chandler scraping failed: {e}")

    def _parse_project_header(self, header, portal_key, base_url) -> Optional[Project]:
        try:
            # 1. Extract Title and ID from Header
            title_link = header.find('a')
            if not title_link:
                return None
                
            full_title_text = title_link.get_text(strip=True)
            
            # ID Extraction
            # We initialize title to full_title_text just in case
            title = full_title_text
            project_id = None
            
            # Regex for "Project No."
            id_match = re.search(r'Project No\.\s*([\w\.]+)', full_title_text, re.IGNORECASE)
            if id_match:
                project_id = id_match.group(1)
                # content after " - " is title
                if " - " in full_title_text:
                    parts = full_title_text.split(" - ", 1)
                    if len(parts) > 1:
                        title = parts[1]
            
            # Generating a unique URL/Anchor
            # The anchor is usually href="#collapse-accordion-..."
            anchor = title_link.get('href', '')
            if anchor.startswith('#'):
                project_url = f"{base_url}{anchor}"
                target_id = anchor.lstrip('#')
            else:
                project_url = base_url
                target_id = None

            # 2. Extract Details from Body
            # The body is usually the NEXT SIBLING of the header with class 'panel-collapse'
            # OR we can find it by ID if we have target_id
            
            body = None
            if target_id:
                # We can't use header.find() because body is not inside header.
                # We can search globally or look for sibling.
                # Searching siblings is safer if IDs are not unique (though they should be).
                body = header.find_next_sibling('div', id=target_id)
                
            if not body:
                body = header.find_next_sibling('div', class_='panel-collapse')

            description_text = ""
            release_date = None
            
            if body:
                body_text = body.get_text(" ", strip=True)
                description_text = body_text
                
                # Try to find ID in body if not in title (common for RFB)
                if not project_id:
                    # Patterns: "Solicitation No:", "Proposal No:", "Project No:"
                    id_patterns = [
                        r'(?:Solicitation|Proposal|Project|Request for Information)\s*No\s*:?\s*([\w-]+)',
                        r'No\s*:\s*([\w-]+)'
                    ]
                    for pat in id_patterns:
                        match = re.search(pat, body_text, re.IGNORECASE)
                        if match:
                            project_id = match.group(1)
                            break
                
                # Try to find Due Date or Release Date
                # We prioritize "Due Date" or "Proposals Due" for date parsing if release date isn't found
                # But typically we want the date the project was posted. 
                # Chandler pages don't seem to show "Posted Date".
                # We will parse the "Due" date as a proxy/metadata, but for "New" detection
                # the system relies on seeing a new ID.
                # So the date field is less critical for liveness, but good for display.
                
                due_date_match = re.search(r'(?:Due|Submittals Due|Proposals Due)\s*:?\s*([A-Z][a-z]+ \d{1,2}, \d{4})', body_text, re.IGNORECASE)
                if due_date_match:
                    try:
                        # Parse "March 11, 2026"
                        date_str = due_date_match.group(1)
                        # We use this as 'release_date' just to have a date. 
                        # Ideally we'd have a separate field, but the Project dataclass is simple.
                        release_date = datetime.strptime(date_str, "%B %d, %Y")
                    except ValueError:
                        pass

            # Fallback ID
            if not project_id:
                # Use a hash of the title if no ID found to ensure we can track it
                # We limit the hash size for readability
                project_id = f"CH-{abs(hash(full_title_text)) % 100000}"

            return Project(
                id=project_id,
                title=title,
                portal=portal_key,
                url=project_url,
                release_date=release_date or datetime.now()
            )
            
        except Exception as e:
            print(f"    ⚠ Error parsing item: {e}")
            return None
