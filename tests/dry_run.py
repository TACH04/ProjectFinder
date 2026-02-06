#!/usr/bin/env python3
"""
Dry run script for ProjectFinder
Scrapes projects and emails those released in the last 7 days.
Bypasses the "previously seen" check.
"""

import sys
from datetime import datetime, timedelta
from typing import List

from config import PORTALS, EMAIL_CONFIG
from scraper.browser import StealthBrowser
from scraper.scraper import OpenGovScraper, Project
from scraper.email_notifier import send_email_notification

def main():
    print("🚀 Starting Dry Run: Checking for projects from the last 7 days...")
    
    all_projects = []
    
    # 1. Scrape all portals
    try:
        with StealthBrowser(headless=True) as browser:
            scraper = OpenGovScraper(browser)
            
            for portal_key, portal_config in PORTALS.items():
                try:
                    projects = scraper.scrape_portal(portal_key, portal_config)
                    all_projects.extend(projects)
                except Exception as e:
                    print(f"\n  ✗ Error scraping {portal_key}: {e}")
                    continue
    except Exception as e:
        print(f"\n✗ Browser error: {e}")
        return 1
    
    if not all_projects:
        print("\n⚠ No projects found at all.")
        return 1

    # 2. Filter for last 7 days
    cutoff_date = datetime.now() - timedelta(days=7)
    recent_projects = []
    
    print(f"\n🔍 Filtering for projects released after {cutoff_date.strftime('%Y-%m-%d')}...")
    
    for p in all_projects:
        url_status = "✓ URL" if p.url else "✗ No URL"
        if p.release_date:
            print(f"  • {p.title[:50]}... ({p.release_date.strftime('%Y-%m-%d')}) [{url_status}]")
            if p.release_date >= cutoff_date:
                recent_projects.append(p)
        else:
            print(f"  • {p.title[:50]}... (No date found) [{url_status}]")
            
    print(f"\n📋 Found {len(recent_projects)} recent projects.")
    
    if not recent_projects:
        print("  ℹ No recent projects to email.")
        return 0
        
    # 3. Send Email
    print("\n📧 Sending email notification...")
    
    if not EMAIL_CONFIG["enabled"]:
        # Force enable for dry run if configured
        if EMAIL_CONFIG["sender_email"] and EMAIL_CONFIG["receiver_email"]:
            print("  ℹ Email disabled in config, but proceeding with dry run usage.")
        else:
            print("  ❌ Email configuration missing (sender/receiver).")
            return 1

    try:
        # We pass recent_projects as 'new_projects' to populate that section of the email
        success = send_email_notification(
            new_projects=recent_projects, 
            todays_projects=[],
            sender_email=EMAIL_CONFIG["sender_email"],
            receiver_email=EMAIL_CONFIG["receiver_email"],
            sender_password=None
        )
        
        if success:
            print("\n✅ Dry run completed successfully! Check your inbox.")
        else:
            print("\n❌ Failed to send email.")
            
    except Exception as e:
        print(f"  ✗ Exception sending email: {e}")

if __name__ == "__main__":
    sys.exit(main())
