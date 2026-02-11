
import sys
import os

# Add parent dir to path so we can import scraper modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.bonfire_scraper import BonfireScraper

def main():
    portal_config = {
        "name": "City of Sedona",
        "url": "https://sedonaaz.bonfirehub.com/portal/?tab=openOpportunities"
    }
    
    scraper = BonfireScraper()
    try:
        projects = scraper.scrape_portal("sedona", portal_config)
        print(f"\nSUCCESS: Found {len(projects)} projects.")
        for p in projects:
            print(f"- {p.title} (ID: {p.id})")
            print(f"  URL: {p.url}")
            print(f"  Date: {p.release_date}")
            
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    main()
