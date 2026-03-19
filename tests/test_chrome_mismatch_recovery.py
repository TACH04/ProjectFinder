#!/usr/bin/env python3
"""
Test: Chrome Version Mismatch Auto-Recovery

Simulates the EXACT failure path the client hit:
  1. Swaps the cached chromedriver with a REAL old version (v134)
  2. Starts StealthBrowser WITHOUT passing version_main (as if detection failed)
  3. This triggers the SessionNotCreatedException
  4. Our recovery code should catch it, clear cache, and retry

Usage:
    python tests/test_chrome_mismatch_recovery.py
"""

import os
import sys
import shutil
import platform
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

OLD_DRIVER_DIR = os.path.join(os.path.dirname(__file__), "chromedriver-mac-arm64")


def get_driver_cache_dir():
    home = os.path.expanduser("~")
    if os.name == 'nt':
        return os.path.join(home, "AppData", "Roaming", "undetected_chromedriver")
    elif platform.system() == 'Darwin':
        return os.path.join(home, "Library", "Application Support", "undetected_chromedriver")
    else:
        return os.path.join(home, ".local", "share", "undetected_chromedriver")


def swap_with_old_driver():
    """Replace the cached chromedriver with a real v134 binary."""
    cache_dir = get_driver_cache_dir()
    
    if not os.path.exists(cache_dir):
        print("  ⚠  Creating driver cache by running browser once...")
        from scraper.browser import StealthBrowser
        try:
            b = StealthBrowser(headless=True)
            b.start()
            b.close()
        except Exception:
            pass
    
    os.makedirs(cache_dir, exist_ok=True)
    
    driver_name = "undetected_chromedriver"
    driver_path = os.path.join(cache_dir, driver_name)
    backup_path = driver_path + ".backup_test"
    
    old_driver = os.path.join(OLD_DRIVER_DIR, "chromedriver")
    if not os.path.exists(old_driver):
        print(f"  ❌ Old chromedriver not found at: {old_driver}")
        return False
    
    if os.path.exists(driver_path):
        print(f"  📦 Backing up current driver")
        shutil.copy2(driver_path, backup_path)
    
    print(f"  🔧 Swapping in OLD v134 chromedriver...")
    shutil.copy2(old_driver, driver_path)
    os.chmod(driver_path, 0o755)
    
    result = subprocess.run([driver_path, "--version"], capture_output=True, text=True, timeout=5)
    print(f"  📋 Cached driver now: {result.stdout.strip()}")
    print()
    return True


def test_auto_recovery():
    """Simulate the exact failure: old driver + no version_main."""
    print("=" * 60)
    print("TEST: Chrome Mismatch Auto-Recovery")
    print("=" * 60)
    print()
    print("Scenario: Chrome is v146, but cached driver is v134,")
    print("and version detection has failed (version_main not passed).")
    print("Expected: Recovery banner → cache clear → retry → success.")
    print()
    
    # Step 1: Poison the cache
    print("STEP 1: Swapping cached driver with old v134...")
    print("-" * 60)
    if not swap_with_old_driver():
        print("❌ ABORTED: Could not set up test.")
        return False
    
    # Step 2: Start browser WITHOUT version_main (simulating detection failure)
    print("STEP 2: Starting browser WITHOUT version_main...")
    print("        (This simulates what happens when version detection fails)")
    print("-" * 60)
    
    import undetected_chromedriver as uc
    from config import BROWSER_SETTINGS
    
    # We need to directly use StealthBrowser but ensure version_main is NOT set.
    # We'll monkey-patch get_chrome_major_version to return None.
    import scraper.browser as browser_module
    original_fn = browser_module.get_chrome_major_version
    browser_module.get_chrome_major_version = lambda: None  # Simulate detection failure
    
    from scraper.browser import StealthBrowser
    browser = None
    saw_recovery = False
    
    try:
        browser = StealthBrowser(headless=True)
        browser.start()
        
        print("-" * 60)
        print()
        print("✅ TEST PASSED: Browser started successfully!")
        print("   If you saw the recovery banner above, auto-fix worked.")
        return True
        
    except Exception as e:
        print("-" * 60)
        print()
        print(f"❌ TEST FAILED: {e}")
        return False
    finally:
        if browser:
            browser.close()
        # Restore original function
        browser_module.get_chrome_major_version = original_fn


if __name__ == "__main__":
    try:
        passed = test_auto_recovery()
        print()
        if passed:
            print("🎉 Auto-recovery is working!")
        else:
            print("💔 Auto-recovery needs work.")
        sys.exit(0 if passed else 1)
    except KeyboardInterrupt:
        print("\nTest cancelled.")
        sys.exit(1)
