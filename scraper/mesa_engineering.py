"""
Scraper for City of Mesa, AZ - Engineering Design Opportunities
Uses StealthBrowser to load the page (site blocks plain requests),
then parses the static HTML table with BeautifulSoup.
"""

import re
from datetime import datetime
from typing import List, Optional
from bs4 import BeautifulSoup

from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper
from scraper.browser import StealthBrowser


@register_scraper("mesa_engineering")
class MesaEngineeringScraper(BaseScraper):
    """Scraper for Mesa AZ Architectural/Engineering Design Opportunities"""

    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        url = portal_config["url"]
        portal_name = portal_config["name"]

        print(f"\n{'='*50}")
        print(f"Scraping (Mesa Engineering): {portal_name}")
        print(f"{'='*50}")

        try:
            # Navigate with the shared browser (site blocks plain requests)
            print(f"  Navigating to: {url}")
            if not self.browser.navigate(url):
                raise PortalScrapingError(f"Failed to load: {portal_name}")

            # Get page source and parse with BeautifulSoup
            page_source = self.browser.get_page_source()
            soup = BeautifulSoup(page_source, "html.parser")
            projects = []

            # The projects live in a responsive table
            table = soup.find("table", class_="sc-responsive-table")
            if not table:
                table = soup.find("table")

            if not table:
                print("  ⚠ Could not find project table")
                return []

            tbody = table.find("tbody")
            if not tbody:
                print("  ⚠ Could not find table body")
                return []

            rows = tbody.find_all("tr")
            print(f"  Found {len(rows)} table rows")

            for row in rows:
                project = self._parse_row(row, portal_key, url)
                if project:
                    projects.append(project)

            print(f"  ✓ Found {len(projects)} active projects")
            return projects

        except PortalScrapingError:
            raise
        except Exception as e:
            print(f"  ✗ Scraping failed: {e}")
            raise PortalScrapingError(f"Mesa Engineering scraping failed: {e}")

    def _parse_row(self, row, portal_key: str, base_url: str) -> Optional[Project]:
        """Parse a single table row into a Project."""
        try:
            cells = row.find_all("td")
            if not cells:
                return None

            # First cell: project title (as a link to the RFQ PDF)
            first_cell = cells[0]
            title_link = first_cell.find("a", class_="document")
            if not title_link:
                title_link = first_cell.find("a")

            if not title_link:
                return None

            full_title = title_link.get_text(strip=True)
            # Strip "(PDF, XXkB)" suffix from title
            full_title = re.sub(r'\s*\(PDF,\s*\d+[A-Z]+\)\s*$', '', full_title).strip()
            pdf_url = title_link.get("href", "")

            # Make relative URLs absolute
            if pdf_url and not pdf_url.startswith("http"):
                pdf_url = f"https://www.mesaaz.gov{pdf_url}"

            # Extract project number from title
            # Patterns: "Project No. CP1298CNTR", "Project Nos. CP1229FM01/CP1229LS04"
            project_id = None
            id_match = re.search(
                r'Project\s+Nos?\.?\s*([\w/]+)',
                full_title,
                re.IGNORECASE
            )
            if id_match:
                project_id = id_match.group(1)

            # Clean up title: remove the project number portion
            title = full_title
            if project_id:
                title = re.sub(
                    r'\s*Project\s+Nos?\.?\s*[\w/]+\s*',
                    '',
                    full_title,
                    flags=re.IGNORECASE
                ).strip()

            # Fallback ID
            if not project_id:
                import hashlib
                # Use MD5 for a stable hash of the title
                hash_object = hashlib.md5(full_title.encode())
                stable_hash = int(hash_object.hexdigest(), 16) % 100000
                project_id = f"MESA-{stable_hash}"

            # Second cell: due date
            release_date = None
            if len(cells) > 1:
                date_text = cells[1].get_text(strip=True)
                release_date = self._parse_date(date_text)

            return Project(
                id=project_id,
                title=title,
                portal=portal_key,
                url=pdf_url or base_url,
                release_date=release_date or datetime.now(),
            )

        except Exception as e:
            print(f"    ⚠ Error parsing row: {e}")
            return None

    @staticmethod
    def _parse_date(text: str) -> Optional[datetime]:
        """Try to parse a date string from various formats."""
        if not text:
            return None

        # Clean up: remove extra info like "by 2 p.m."
        clean = re.sub(r',?\s*by\s+.*$', '', text, flags=re.IGNORECASE).strip()

        formats = [
            "%B %d, %Y",     # "January 13, 2026"
            "%m/%d/%Y",      # "01/13/2026"
        ]

        for fmt in formats:
            try:
                return datetime.strptime(clean, fmt)
            except ValueError:
                continue

        return None
