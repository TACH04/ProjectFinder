import os
import sys
import time

# Add parent directory to path to allow importing scraper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper.browser import StealthBrowser

def test_browser_health():
    print("Testing StealthBrowser initialization...")
    browser = StealthBrowser(headless=True)
    browser.start()
    
    # 1. Test navigation
    print("\nTesting navigation...")
    success = browser.navigate("https://example.com")
    print(f"Navigation success: {success}")
    assert success, "Navigation to example.com failed"
    
    # 2. Test healthy status
    print("\nTesting is_healthy()...")
    is_healthy = browser.is_healthy()
    print(f"Browser healthy: {is_healthy}")
    assert is_healthy, "Browser should be healthy after normal navigation"
    
    # 3. Simulate failure by closing the driver
    print("\nSimulating browser failure (closing driver manually)...")
    browser.driver.quit()
    
    # 4. Check health again
    is_healthy_now = browser.is_healthy()
    print(f"Browser healthy after quitting: {is_healthy_now}")
    assert not is_healthy_now, "Browser should NOT be healthy after quitting"
    
    # 5. Test restart
    print("\nTesting restart()...")
    restart_success = browser.restart()
    print(f"Restart success: {restart_success}")
    assert restart_success, "Browser restart failed"
    
    # 6. Check health after restart
    is_finally_healthy = browser.is_healthy()
    print(f"Browser healthy after restart: {is_finally_healthy}")
    assert is_finally_healthy, "Browser should be healthy after restart"
    
    print("\nAll health tests passed! Closing browser.")
    browser.close()

if __name__ == "__main__":
    try:
        test_browser_health()
        print("\n✅ test_browser_health PASS")
    except AssertionError as e:
        print(f"\n❌ test_browser_health FAIL: {e}")
        sys.exit(1)
