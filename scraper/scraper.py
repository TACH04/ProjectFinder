"""
Core scraping logic for OpenGov Procurement portals
"""

import time
import re
from datetime import datetime, date
from dataclasses import dataclass
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from scraper.browser import StealthBrowser


@dataclass
class Project:
    """Represents a procurement project"""
    id: str
    title: str
    release_date: str
    status: str
    portal: str
    url: Optional[str] = None
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "status": self.status,
            "portal": self.portal,
            "url": self.url,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        return cls(**data)
    
    def is_from_today(self) -> bool:
        """Check if this project was released today"""
        try:
            # Parse common date formats
            for fmt in ["%m/%d/%Y", "%Y-%m-%d", "%m-%d-%Y", "%B %d, %Y"]:
                try:
                    release = datetime.strptime(self.release_date, fmt).date()
                    return release == date.today()
                except ValueError:
                    continue
            return False
        except Exception:
            return False


class OpenGovScraper:
    """Scraper for OpenGov Procurement portals"""
    
    def __init__(self, browser: StealthBrowser):
        self.browser = browser
        
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from a portal
        
        Steps:
        1. Navigate to portal
        2. Click "Active" status filter
        3. Double-click "Release Date" to sort newest first
        4. Click Search
        5. Extract project data
        """
        url = portal_config["url"]
        portal_name = portal_config["name"]
        
        print(f"\n{'='*50}")
        print(f"Scraping: {portal_name}")
        print(f"{'='*50}")
        
        # Navigate to portal
        if not self.browser.navigate(url):
            print(f"  ✗ Failed to load portal: {portal_name}")
            return []
        
        # Give the React app time to fully load
        time.sleep(3)
        
        # Step 1: Click "Active" status filter
        print("  Step 1: Selecting 'Active' filter...")
        if not self._select_active_filter():
            print("  ⚠ Could not find Active filter, continuing anyway...")
        
        # Step 2: Sort by Release Date (newest first = double click)
        print("  Step 2: Sorting by Release Date (newest first)...")
        if not self._sort_by_release_date():
            print("  ⚠ Could not sort by release date, continuing anyway...")
        
        # Step 3: Click Search button
        print("  Step 3: Triggering search...")
        if not self._click_search():
            print("  ⚠ Could not click search, continuing anyway...")
        
        # Wait for results to load
        time.sleep(2)
        
        # Step 4: Extract projects
        print("  Step 4: Extracting projects...")
        projects = self._extract_projects(portal_key)
        
        print(f"  ✓ Found {len(projects)} active projects")
        return projects
    
    def _select_active_filter(self) -> bool:
        """Click the Active status filter"""
        # Try multiple selectors for the Active button/checkbox
        selectors = [
            # Button with text "Active"
            "//button[contains(text(), 'Active')]",
            "//span[contains(text(), 'Active')]/parent::button",
            # Chip/tag style
            "//div[contains(@class, 'chip') and contains(text(), 'Active')]",
            # Checkbox or radio
            "//label[contains(text(), 'Active')]",
            "//input[@value='active']/parent::label",
            # Status dropdown option
            "//li[contains(text(), 'Active')]",
            "//div[@role='option' and contains(text(), 'Active')]",
            # Generic clickable with Active text
            "//*[contains(@class, 'status') and contains(text(), 'Active')]",
        ]
        
        for selector in selectors:
            try:
                elements = self.browser.find_elements(By.XPATH, selector)
                for elem in elements:
                    if elem.is_displayed():
                        elem.click()
                        time.sleep(1)
                        return True
            except Exception:
                continue
        
        return False
    
    def _sort_by_release_date(self) -> bool:
        """Double-click Release Date header to sort descending"""
        selectors = [
            # Table header
            "//th[contains(text(), 'Release')]",
            "//th[contains(text(), 'release')]",
            "//div[contains(@class, 'header') and contains(text(), 'Release')]",
            # Sortable column
            "//*[contains(@class, 'sort') and contains(text(), 'Release')]",
            "//button[contains(text(), 'Release Date')]",
            # Generic clickable
            "//*[contains(text(), 'Release Date')]",
        ]
        
        for selector in selectors:
            try:
                elements = self.browser.find_elements(By.XPATH, selector)
                for elem in elements:
                    if elem.is_displayed():
                        # Double click for descending sort
                        elem.click()
                        time.sleep(0.5)
                        elem.click()
                        time.sleep(1)
                        return True
            except Exception:
                continue
        
        return False
    
    def _click_search(self) -> bool:
        """Click the Search button"""
        selectors = [
            "//button[contains(text(), 'Search')]",
            "//button[@type='submit']",
            "//input[@type='submit']",
            "//button[contains(@class, 'search')]",
            "//*[@aria-label='Search']",
        ]
        
        for selector in selectors:
            try:
                elements = self.browser.find_elements(By.XPATH, selector)
                for elem in elements:
                    if elem.is_displayed():
                        elem.click()
                        time.sleep(1)
                        return True
            except Exception:
                continue
        
        return False
    
    def _extract_projects(self, portal_key: str) -> List[Project]:
        """Extract project data from the results table/list"""
        projects = []
        
        # Try to find project rows in various table/list structures
        row_selectors = [
            "//tr[contains(@class, 'row')]",
            "//div[contains(@class, 'project-row')]",
            "//div[contains(@class, 'solicitation')]",
            "//a[contains(@href, '/portal/') and contains(@href, '/projects/')]",
            "//table//tbody//tr",
            "//div[contains(@class, 'list-item')]",
        ]
        
        for selector in row_selectors:
            try:
                rows = self.browser.find_elements(By.XPATH, selector)
                if rows:
                    print(f"    Found {len(rows)} rows with selector: {selector[:50]}...")
                    for row in rows:
                        project = self._parse_project_row(row, portal_key)
                        if project:
                            projects.append(project)
                    if projects:
                        break
            except Exception as e:
                continue
        
        # If no structured data, try to extract from page source
        if not projects:
            projects = self._extract_from_page_source(portal_key)
        
        return projects
    
    def _parse_project_row(self, row, portal_key: str) -> Optional[Project]:
        """Parse a single project row"""
        try:
            # Get all text content
            text = row.text.strip()
            if not text or len(text) < 10:
                return None
            
            # Try to find a link for the project URL
            url = None
            try:
                link = row.find_element(By.TAG_NAME, "a")
                url = link.get_attribute("href")
            except NoSuchElementException:
                pass
            
            # Try to extract structured data
            # Look for common patterns in the text
            lines = text.split('\n')
            
            # First line is usually the title
            title = lines[0] if lines else text[:100]
            
            # Try to find a project ID (usually numeric or alphanumeric pattern)
            id_match = re.search(r'(?:ID|#|Project)\s*:?\s*(\d+[-\w]*)', text, re.IGNORECASE)
            project_id = id_match.group(1) if id_match else f"_{hash(text) % 100000}"
            
            # Try to find a date
            date_match = re.search(r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})', text)
            release_date = date_match.group(1) if date_match else "Unknown"
            
            return Project(
                id=project_id,
                title=title[:200],
                release_date=release_date,
                status="Active",
                portal=portal_key,
                url=url,
            )
        except Exception as e:
            return None
    
    def _extract_from_page_source(self, portal_key: str) -> List[Project]:
        """Fallback: extract project data from raw page source"""
        projects = []
        source = self.browser.get_page_source()
        
        # Look for JSON data embedded in the page
        json_patterns = [
            r'"title"\s*:\s*"([^"]+)".*?"id"\s*:\s*"?(\d+)"?',
            r'"projectTitle"\s*:\s*"([^"]+)"',
            r'"solicitation(?:Title|Name)"\s*:\s*"([^"]+)"',
        ]
        
        for pattern in json_patterns:
            matches = re.findall(pattern, source, re.IGNORECASE)
            for match in matches[:20]:  # Limit to 20 projects
                if isinstance(match, tuple):
                    title, project_id = match[0], match[1] if len(match) > 1 else str(len(projects))
                else:
                    title, project_id = match, str(len(projects))
                
                projects.append(Project(
                    id=project_id,
                    title=title,
                    release_date="Unknown",
                    status="Active",
                    portal=portal_key,
                ))
        
        return projects
