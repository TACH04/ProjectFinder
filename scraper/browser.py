"""
Stealth browser automation using undetected-chromedriver for Cloudflare bypass
"""

import time
import random
import os

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config import BROWSER_SETTINGS


class StealthBrowser:
    """Browser wrapper with Cloudflare bypass capabilities using undetected-chromedriver"""
    

    def __init__(self, headless: bool = None):
        self.headless = headless if headless is not None else BROWSER_SETTINGS["headless"]
        self.driver = None
        self.wait_timeout = BROWSER_SETTINGS["wait_timeout"]
        
    def start(self):
        """Initialize the undetected Chrome browser"""
        options = uc.ChromeOptions()
        
        if self.headless:
            print("  👻 Setting background mode (window off-screen)...")
            # We avoid true headless mode because Cloudflare detects it easily.
            # Instead, we run a normal window but move it off-screen.
            options.add_argument("--window-position=-10000,0")
        
        # Human-like settings
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Use project-local data directory
        user_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".chrome_profile")
        os.makedirs(user_data_dir, exist_ok=True)
        
        self.driver = uc.Chrome(
            options=options,
            user_data_dir=user_data_dir,
            use_subprocess=True,
            version_main=144,  # Match Chrome version 144
        )
        
        # Force window off-screen if in background mode
        if self.headless:
            try:
                self.driver.set_window_position(-10000, 0)
            except Exception:
                pass
                
        # Set page load timeout
        try:
            self.driver.set_page_load_timeout(BROWSER_SETTINGS.get("page_load_timeout", 30))
        except Exception:
            pass
        
        return self
    
    def __enter__(self):
        return self.start()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        
    def close(self):
        """Close the browser"""
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
            self.driver = None
    
    def navigate(self, url: str) -> bool:
        """Navigate to URL and wait for Cloudflare to pass"""
        print(f"  Navigating to {url}...")
        try:
            self.driver.get(url)
        except TimeoutException:
            print(f"  ✗ Page load timed out after {BROWSER_SETTINGS.get('page_load_timeout', 30)}s")
            # If we timeout, we should probably return False so the scraper knows it failed
            # We might need to stop loading? 
            try:
                self.driver.execute_script("window.stop();")
            except Exception:
                pass
            return False
        except Exception as e:
            print(f"  ✗ Navigation failed: {e}")
            return False
        
        # Wait for Cloudflare challenge to complete
        if not self._wait_for_cloudflare():
            return False
            
        return True
    
    def _wait_for_cloudflare(self) -> bool:
        """Wait for Cloudflare verification to complete"""
        # Quick check: if we are not on a Cloudflare page, return immediately without delay
        # This assumes driver.get() has mostly loaded the page or at least the title
        try:
            title = self.driver.title.lower()
            if "just a moment" not in title and "checking" not in title:
                return True
        except Exception:
            pass

        max_wait = BROWSER_SETTINGS["cloudflare_wait"]
        start_time = time.time()
        
        print("  Checking for Cloudflare...")
        
        while time.time() - start_time < max_wait:
            try:
                title = self.driver.title.lower()
                # Check if we're past Cloudflare
                if "just a moment" not in title and "checking" not in title:
                    print("  ✓ Cloudflare bypassed")
                    self._human_delay(1, 2)  # Let page fully settle after a bypass
                    return True
                
                # Attempt to find and click the challenge checkbox
                # This is a best-effort attempt as Cloudflare changes often
                try:
                    # Look for shadow host
                    shadow_host = self.driver.find_element(By.CSS_SELECTOR, "#turnstile-wrapper")
                    if shadow_host:
                        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
                        if shadow_root:
                            checkbox = shadow_root.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
                            if checkbox:
                                checkbox.click()
                                print("  ✓ Attempted to click Cloudflare checkbox")
                except Exception:
                    # Silent failure on auto-click attempt, as it's optional
                    pass

            except Exception:
                pass
            
            if int(time.time() - start_time) % 5 == 0:
                 print("  ⚠ Cloudflare detected! Please manually click the checkbox if needed...")
            time.sleep(1)
        
        print("  ✗ Cloudflare bypass timeout - try running without --headless")
        return False
    
    def wait_for_element(self, by: By, value: str, timeout: int = None) -> bool:
        """Wait for an element to be present"""
        timeout = timeout or self.wait_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False
    
    def click_element(self, by: By, value: str, timeout: int = None):
        """Wait for element and click it with human-like behavior"""
        timeout = timeout or self.wait_timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            self._human_delay(0.1, 0.3)
            element.click()
            return True
        except TimeoutException:
            print(f"  ✗ Could not find clickable element: {value}")
            return False
    
    def find_elements(self, by: By, value: str):
        """Find all matching elements"""
        return self.driver.find_elements(by, value)
    
    def find_element(self, by: By, value: str):
        """Find a single element"""
        return self.driver.find_element(by, value)
    
    def get_page_source(self) -> str:
        """Get the current page HTML source"""
        return self.driver.page_source
    
    def _human_delay(self, min_seconds: float = 0.5, max_seconds: float = 1.5):
        """Add random delay to simulate human behavior"""
        # Reduced default delay to be faster
        time.sleep(random.uniform(min_seconds, max_seconds))
        
    def save_screenshot(self, path: str):
        """Save a screenshot of the current page"""
        if self.driver:
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                self.driver.save_screenshot(path)
                print(f"  📸 Screenshot saved to {path}")
            except Exception as e:
                print(f"  ⚠ Failed to save screenshot: {e}")
