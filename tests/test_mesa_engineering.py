
import sys
import os

# Add parent dir to path so we can import scraper modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.browser import StealthBrowser
from scraper.mesa_engineering import MesaEngineeringScraper

def main():
    config = {
        "key": "mesa_engineering",
        "name": "City of Mesa - Engineering RFQs",
        "url": "https://www.mesaaz.gov/Business-Development/Engineering/Architectural-Engineering-Design-Opportunities"
    }

    with StealthBrowser(headless=False) as browser:
        scraper = MesaEngineeringScraper(browser)

        print(f"\nTesting {config['name']}...")
        try:
            projects = scraper.scrape_portal(config["key"], config)
            print(f"\nSUCCESS: Found {len(projects)} projects.")
            for p in projects:
                print(f"- {p.title}")
                print(f"  ID: {p.id}")
                print(f"  Date: {p.release_date}")
                print(f"  URL: {p.url}")
                print("-" * 40)

            if not projects:
                print("WARNING: No projects found. Check selectors.")

        except Exception as e:
            print(f"FAILED: {e}")

if __name__ == "__main__":
    main()
