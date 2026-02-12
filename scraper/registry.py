from typing import Dict, Type, Optional
from scraper.base import BaseScraper

# Registry to hold scraper classes
# Key: scraper_type (str), Value: Scraper Class
SCRAPER_REGISTRY: Dict[str, Type[BaseScraper]] = {}

def register_scraper(scraper_type: str):
    """Decorator to register a scraper class"""
    def decorator(cls: Type[BaseScraper]):
        SCRAPER_REGISTRY[scraper_type] = cls
        return cls
    return decorator

def get_scraper_class(scraper_type: str) -> Optional[Type[BaseScraper]]:
    """Retrieve a scraper class by type"""
    return SCRAPER_REGISTRY.get(scraper_type)
