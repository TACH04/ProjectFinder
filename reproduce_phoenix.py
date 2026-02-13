#!/usr/bin/env python3
"""
Reproduction script for Phoenix scraper issues.
"""
import os
import sys
import time
import logging
from datetime import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import PORTALS, BROWSER_SETTINGS
from scraper.browser import StealthBrowser
from scraper.opengov import OpenGovScraper
from run_scraper import capture_screenshots_scroll

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("ReproducePhoenix")

def main():
    portal_key = "phoenix"
    portal_config = PORTALS[portal_key]
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.join("logs", f"reproduce_phoenix_{timestamp}")
    os.makedirs(output_dir, exist_ok=True)
    
    logger.info(f"🚀 Starting reproduction for {portal_key}...")
    logger.info(f"   Output directory: {output_dir}")
    
    # Force visible browser for debugging (unless overridden)
    headless = False 
    
    try:
        with StealthBrowser(headless=headless) as browser:
            scraper = OpenGovScraper(browser)
            
            # 1. Scrape Project List
            logger.info("Step 1: Scraping project list...")
            projects = scraper.scrape_portal(portal_key, portal_config)
            
            logger.info(f"   ✓ Found {len(projects)} projects")
            
            # Save project list
            with open(os.path.join(output_dir, "projects.txt"), "w") as f:
                for p in projects:
                    f.write(f"[{p.id}] {p.title}\n")
                    f.write(f"   URL: {p.url}\n")
                    f.write(f"   Date: {p.release_date}\n\n")
            
            # 2. Save HTML Source
            logger.info("Step 2: Saving Page Source...")
            source = browser.get_page_source()
            with open(os.path.join(output_dir, "source.html"), "w", encoding='utf-8') as f:
                f.write(source)
            logger.info(f"   ✓ Saved source.html ({len(source)} bytes)")
            
            # 3. Capture Screenshots
            logger.info("Step 3: Capturing Screenshots...")
            images = capture_screenshots_scroll(browser, output_dir, portal_key)
            logger.info(f"   ✓ Captured {len(images)} screenshots")

            logger.info("--------------------------------------------------")
            logger.info(f"✅ Reproduction run complete. Check {output_dir}")
            
    except Exception as e:
        logger.error(f"✗ Error: {e}", exc_info=True)

if __name__ == "__main__":
    main()
