
import sys
import os

# Add parent dir to path so we can import scraper modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.chandler_scraper import ChandlerScraper

def main():
    # Test Configs
    configs = [
        {
            "key": "chandler_rfq",
            "name": "City of Chandler - RFQ",
            "url": "https://www.chandleraz.gov/business/vendor-services/capital-projects/request-for-qualifications"
        },
        {
            "key": "chandler_rfb",
            "name": "City of Chandler - RFB",
            "url": "https://www.chandleraz.gov/business/vendor-services/purchasing/requests-for-bids-and-proposals"
        }
    ]
    
    scraper = ChandlerScraper()
    
    for config in configs:
        print(f"\nTesting {config['name']}...")
        try:
            projects = scraper.scrape_portal(config["key"], config)
            print(f"SUCCESS: Found {len(projects)} projects.")
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
