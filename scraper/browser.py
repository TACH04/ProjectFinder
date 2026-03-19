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

import subprocess
import re
import os
import sys

from config import BROWSER_SETTINGS


def get_chrome_major_version():
    """Detect local Chrome major version to pass to undetected-chromedriver.
    
    Uses multiple fallback methods on Windows because some environments
    (e.g., Microsoft Store Python) have restricted registry access.
    """
    if os.name == 'nt':
        # Windows - Method 1: Registry (fastest)
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
            version, _ = winreg.QueryValueEx(key, 'version')
            return int(version.split('.')[0])
        except Exception:
            pass

        # Windows - Method 2: Check chrome.exe directly via WMIC
        try:
            chrome_paths = [
                os.path.join(os.environ.get('PROGRAMFILES', 'C:\\Program Files'), 'Google', 'Chrome', 'Application', 'chrome.exe'),
                os.path.join(os.environ.get('PROGRAMFILES(X86)', 'C:\\Program Files (x86)'), 'Google', 'Chrome', 'Application', 'chrome.exe'),
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Google', 'Chrome', 'Application', 'chrome.exe'),
            ]
            for chrome_path in chrome_paths:
                if os.path.exists(chrome_path):
                    escaped = chrome_path.replace('\\', '\\\\')
                    result = subprocess.run(
                        f'wmic datafile where name="{escaped}" get Version /value',
                        capture_output=True, text=True, shell=True, timeout=10
                    )
                    match = re.search(r'Version=(\d+)\.', result.stdout)
                    if match:
                        return int(match.group(1))
        except Exception:
            pass

        # Windows - Method 3: PowerShell (last resort)
        try:
            result = subprocess.run(
                ['powershell', '-Command',
                 '(Get-Item "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe").VersionInfo.FileVersion'],
                capture_output=True, text=True, timeout=10
            )
            match = re.search(r'(\d+)\.', result.stdout.strip())
            if match:
                return int(match.group(1))
        except Exception:
            pass

        print("  ⚠ Could not detect Chrome version on Windows. Driver version mismatch may occur.")
        return None

    elif sys.platform == 'darwin':
        # macOS
        try:
            process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
            version = process.communicate()[0].decode('utf-8').strip()
            match = re.search(r'Chrome (\d+)\.', version)
            if match:
                return int(match.group(1))
        except Exception as e:
            print(f"  ⚠ Failed to detect Chrome version: {e}")
    else:
        # Linux
        try:
            process = subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE)
            version = process.communicate()[0].decode('utf-8').strip()
            match = re.search(r'Chrome (\d+)\.', version)
            if match:
                return int(match.group(1))
        except Exception as e:
            print(f"  ⚠ Failed to detect Chrome version: {e}")

    return None

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
            print("  👻 Setting background mode (small window in corner)...")
            # We avoid true headless mode because Cloudflare detects it easily.
            # Ghost mode = small, ignorable window in top-right corner.
            options.add_argument("--window-size=400,300")
        else:
            # Human-like settings for visible mode
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Use project-local data directory
        user_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".chrome_profile")
        os.makedirs(user_data_dir, exist_ok=True)
        
        # Determine the major version dynamically to avoid crashes
        version_main = get_chrome_major_version()
        
        kwargs = {
            "options": options,
            "user_data_dir": user_data_dir,
            "use_subprocess": True,
        }
        if version_main:
            kwargs["version_main"] = version_main
            
        try:
            self.driver = uc.Chrome(**kwargs)
        except Exception as e:
            error_msg = str(e)
            if "This version of ChromeDriver only supports Chrome version" in error_msg:
                print()
                print("  ╔══════════════════════════════════════════════════════════╗")
                print("  ║  ⚠  Chrome version mismatch detected!                  ║")
                print("  ║  Your Chrome browser updated but the cached driver      ║")
                print("  ║  is outdated. Clearing cache and retrying...            ║")
                print("  ╚══════════════════════════════════════════════════════════╝")
                print()
                
                # Clear the stale chromedriver cache
                import shutil
                import platform
                home = os.path.expanduser("~")
                if os.name == 'nt':
                    driver_cache = os.path.join(home, "AppData", "Roaming", "undetected_chromedriver")
                elif platform.system() == 'Darwin':
                    driver_cache = os.path.join(home, "Library", "Application Support", "undetected_chromedriver")
                else:
                    driver_cache = os.path.join(home, ".local", "share", "undetected_chromedriver")

                if os.path.exists(driver_cache):
                    try:
                        shutil.rmtree(driver_cache)
                        print("  🧹 Cleared stale ChromeDriver cache.")
                    except Exception as cache_err:
                        print(f"  ⚠ Could not clear cache: {cache_err}")

                # Also clear the browser profile in case it's corrupted
                if os.path.exists(user_data_dir):
                    try:
                        shutil.rmtree(user_data_dir)
                        os.makedirs(user_data_dir, exist_ok=True)
                        print("  🧹 Reset browser profile.")
                    except Exception:
                        pass

                # Retry with fresh driver
                print("  🔄 Downloading fresh ChromeDriver and retrying...")
                print()
                try:
                    self.driver = uc.Chrome(**kwargs)
                    print("  ✅ Browser started successfully after auto-fix!")
                except Exception as retry_err:
                    print(f"  ❌ Retry failed: {retry_err}")
                    print("  💡 Try manually updating Chrome or running with --reset-browser")
                    raise
            else:
                raise

        
        # Position window in top-right corner for ghost mode
        if self.headless:
            try:
                # Get screen dimensions to position in top-right
                screen_width = self.driver.execute_script("return window.screen.width;")
                window_width = 400
                
                # Position in top-right corner (with small margin)
                x_position = screen_width - window_width - 10
                self.driver.set_window_position(x_position, 0)
                self.driver.set_window_size(window_width, 300)
                print(f"  ✓ Browser positioned at top-right corner ({window_width}x300)")
            except Exception as e:
                print(f"  ⚠ Could not position window: {e}")
                # Fallback: just use a reasonable position
                try:
                    self.driver.set_window_position(1400, 0)
                    self.driver.set_window_size(400, 300)
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
            # Set a script timeout just in case
            self.driver.set_script_timeout(10)
            
            self.driver.get(url)
            # Give the browser a moment to process the navigation
            time.sleep(3)
            
            # Check if we landed on a blank page (indicates a totally broken session)
            current_url = self.driver.current_url
            
            if current_url == "about:blank" or current_url.startswith("data:"):
                print(f"  ✗ Navigation failed: Blank page detected ({current_url})")
                return False
                
        except TimeoutException:
            print(f"  ✗ Page load timed out after {BROWSER_SETTINGS.get('page_load_timeout', 30)}s")
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
        print("  Checking for Cloudflare...")
        
        # Give the browser a tiny bit more time to at least set the title
        for _ in range(5):
            title = self.driver.title.strip()
            if title:
                break
            time.sleep(1)
            
        title = self.driver.title.lower()
        if title and "just a moment" not in title and "checking" not in title:
            # We have a real title and it's not a challenge page
            return True

        max_wait = BROWSER_SETTINGS["cloudflare_wait"]
        start_time = time.time()
        
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
    
    def ensure_corner_position(self):
        """Ensure window stays in top-right corner (for ghost mode)."""
        if self.headless and self.driver:
            try:
                screen_width = self.driver.execute_script("return window.screen.width;")
                self.driver.set_window_position(screen_width - 410, 0)
                self.driver.set_window_size(400, 300)
            except Exception:
                pass

    def is_healthy(self) -> bool:
        """Check if the browser process is still responsive."""
        if not self.driver:
            return False
        try:
            # Simple check to see if the driver can execute a script
            self.driver.execute_script("return 1;")
            return True
        except Exception as e:
            print(f"  ⚠ Browser health check failed: {e}")
            return False

    def restart(self) -> bool:
        """Restart the browser instance."""
        print("  🔄 Restarting browser instance...")
        self.close()
        try:
            self.start()
            return True
        except Exception as e:
            print(f"  ✗ Failed to restart browser: {e}")
            return False
