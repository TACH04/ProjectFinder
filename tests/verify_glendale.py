import logging
from scraper.glendale import GlendaleScraper
from scraper.browser import StealthBrowser

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_glendale():
    print("Initializing browser...")
    browser = StealthBrowser(headless=False)
    browser.start()  # Must call start() to initialize the Chrome driver
    scraper = GlendaleScraper(browser)
    
    config = {
        "url": "https://glendaleazvendors.munisselfservice.com/Vendors/VBids/Default.aspx",
        "name": "City of Glendale"
    }
    
    try:
        print("Starting scrape...")
        projects = scraper.scrape_portal("glendaleaz", config)
        print(f"\nFound {len(projects)} projects")
        
        for p in projects:
            print(f"  - [{p.id}] {p.title} (due: {p.release_date})")
            if p.url:
                print(f"    URL: {p.url}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\nClosing browser...")
        browser.close()

if __name__ == "__main__":
    test_glendale()
