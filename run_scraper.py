#!/usr/bin/env python3
"""
Production script for ProjectFinder
Scrapes projects and emails ONLY if new projects are detected.
"""

import sys
from datetime import datetime

from config import PORTALS, BROWSER_SETTINGS
from scraper.browser import StealthBrowser
from scraper.scraper import OpenGovScraper
from scraper.notifications import check_for_new_projects, notify_new_projects
from scraper.email_notifier import send_email_notification

def main():
    print(f"🚀 Starting Scraper Run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    all_projects = []
    
    # 1. Scrape all portals
    try:
        # Use headless mode from config (usually True for production)
        headless = BROWSER_SETTINGS["headless"]
        
        with StealthBrowser(headless=headless) as browser:
            scraper = OpenGovScraper(browser)
            
            for portal_key, portal_config in PORTALS.items():
                try:
                    projects = scraper.scrape_portal(portal_key, portal_config)
                    all_projects.extend(projects)
                except Exception as e:
                    print(f"\n  ✗ Error scraping {portal_key}: {e}")
                    continue
                    
    except Exception as e:
        print(f"\n✗ Browser/Scraper error: {e}")
        return 1
    
    if not all_projects:
        print("\n⚠ No active projects found on any portal.")
        return 0

    # 2. Check for new projects
    print("\n🔍 Checking for new projects against database...")
    new_projects, _ = check_for_new_projects(all_projects)
    
    # 3. Print CLI summary
    notify_new_projects(new_projects, [])
    
    # 4. Send Email if there are new projects
    if new_projects:
        print(f"\n📧 Sending email notification for {len(new_projects)} new projects...")
        if send_email_notification(new_projects):
            print("  ✓ Email notification sent successfully!")
        else:
            print("  ✗ Failed to send email notification.")
    else:
        print("\n😴 No new projects to notify about.")

    print("\n✅ Run completed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
