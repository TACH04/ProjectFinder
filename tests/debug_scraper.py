from scraper.browser import StealthBrowser
from selenium.webdriver.common.by import By
import time
import os

def main():
    print("Opening browser... (Headless=False)")
    # Force headless=False so user can see/interact
    with StealthBrowser(headless=False) as browser:
        url = "https://procurement.opengov.com/portal/phoenix"
        print(f"Navigating to {url}...")
        browser.navigate(url)
        
        print("\n" + "="*50)
        print("ACTION REQUIRED:")
        print("Please verify the page is loaded in the Chrome window.")
        print("If there is a Cloudflare check, please complete it manually.")
        print("Once the project list is visible, press ENTER in this terminal.")
        print("="*50 + "\n")
        
        input("Press Enter to continue...")
        
        print("Saving page source to 'debug_page_source.html'...")
        with open("debug_page_source.html", "w", encoding="utf-8") as f:
            f.write(browser.get_page_source())
        print(f"Saved to {os.path.abspath('debug_page_source.html')}")
        
        # Test Selectors
        print("\nTesting Selectors...")
        
        # 1. Active Filter
        print("Looking for Active Filter...")
        active_selectors = [
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
        found = False
        for sel in active_selectors:
            try:
                elems = browser.find_elements(By.XPATH, sel)
                visible = [e for e in elems if e.is_displayed()]
                if visible:
                    print(f"  [SUCCESS] Found Active filter with: {sel}")
                    found = True
                    break
            except Exception:
                pass
                
        if not found:
            print("  [FAILED] Could not find Active filter with known selectors.")

        # 2. Release Date Header
        print("Looking for Release Date Header...")
        date_selectors = [
             # Specific React Table structure (User provided)
            "//div[@role='columnheader' and .//div[contains(text(), 'Release Date')]]",
            "//div[contains(@class, 'rt-resizable-header-content') and contains(text(), 'Release Date')]",
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
        found = False
        for sel in date_selectors:
            try:
                elems = browser.find_elements(By.XPATH, sel)
                visible = [e for e in elems if e.is_displayed()]
                if visible:
                    print(f"  [SUCCESS] Found Release Date header with: {sel}")
                    found = True
                    break
            except Exception:
                pass

        if not found:
             print("  [FAILED] Could not find Release Date header with known selectors.")
             
        time.sleep(2)
        print("\nDebug session finished. Please send the 'debug_page_source.html' file and these logs to me.")

if __name__ == "__main__":
    main()
