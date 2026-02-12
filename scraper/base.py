from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Protocol

# We use a Protocol for the browser to avoid circular imports 
# or we can just type it as 'Any' if we want to be loose, 
# but Protocol is cleaner.
class BrowserProtocol(Protocol):
    def navigate(self, url: str) -> bool: ...
    def get_page_source(self) -> str: ...
    # Add other methods as needed

@dataclass
class Project:
    """Represents a procurement project"""
    id: str
    title: str
    portal: str  # Portal key (e.g., 'phoenix', 'surpriseaz')
    url: Optional[str] = None
    release_date: Optional[datetime] = None
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "portal": self.portal,
            "url": self.url,
            "release_date": self.release_date.isoformat() if self.release_date else None,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        # Handle old data format that may have extra fields
        release_date = None
        if data.get("release_date"):
            try:
                release_date = datetime.fromisoformat(data["release_date"])
            except ValueError:
                pass
                
        return cls(
            id=data["id"],
            title=data["title"],
            portal=data["portal"],
            url=data.get("url"),
            release_date=release_date,
        )

class PortalScrapingError(Exception):
    """Raised when scraping a portal fails (e.g. timeout, Cloudflare block)"""
    pass

class BaseScraper(ABC):
    """Abstract base class for all scrapers"""
    
    def __init__(self, browser: Optional[BrowserProtocol] = None):
        self.browser = browser

    @abstractmethod
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        """
        Scrape active projects from a portal.
        
        Args:
            portal_key: The unique key for the portal (e.g. 'phoenix')
            portal_config: Dictionary containing portal configuration (url, name, etc)
            
        Returns:
            List of Project objects
            
        Raises:
            PortalScrapingError: If scraping fails
        """
        pass
