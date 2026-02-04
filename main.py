#!/usr/bin/env python3
"""
ProjectFinder - OpenGov Procurement Scraper
Checks for new government procurement projects from configured portals.

Usage:
    python main.py                    # Check all configured portals
    python main.py --portal phoenix   # Check specific portal
    python main.py --headless         # Run in headless mode
"""

import argparse
import sys

from config import PORTALS
from scraper.browser import StealthBrowser
from scraper.scraper import OpenGovScraper
from scraper.notifications import check_for_new_projects, notify_new_projects


def main():
    parser = argparse.ArgumentParser(
        description="Check for new government procurement projects"
    )
    parser.add_argument(
        "--portal", "-p",
        choices=list(PORTALS.keys()),
        help="Specific portal to check (default: all)"
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (may reduce bypass success)"
    )
    parser.add_argument(
        "--list-portals",
        action="store_true",
        help="List all configured portals"
    )
    
    args = parser.parse_args()
    
    # List portals mode
    if args.list_portals:
        print("Configured portals:")
        for key, config in PORTALS.items():
            print(f"  {key}: {config['name']}")
            print(f"         {config['url']}")
        return 0
    
    # Determine which portals to check
    portals_to_check = {args.portal: PORTALS[args.portal]} if args.portal else PORTALS
    
    print(f"\n🔍 ProjectFinder - Checking {len(portals_to_check)} portal(s)...")
    
    all_projects = []
    
    try:
        with StealthBrowser(headless=args.headless) as browser:
            scraper = OpenGovScraper(browser)
            
            for portal_key, portal_config in portals_to_check.items():
                try:
                    projects = scraper.scrape_portal(portal_key, portal_config)
                    all_projects.extend(projects)
                except Exception as e:
                    print(f"\n  ✗ Error scraping {portal_key}: {e}")
                    continue
    
    except Exception as e:
        print(f"\n✗ Browser error: {e}")
        print("\nTroubleshooting:")
        print("  1. Make sure Chrome is installed")
        print("  2. Try running without --headless flag")
        print("  3. Check your internet connection")
        return 1
    
    # Check for new projects
    if all_projects:
        new_projects, _ = check_for_new_projects(all_projects)
        summary = notify_new_projects(new_projects, [])
        
        # Send email if enabled and there are relevant projects
        from config import EMAIL_CONFIG
        from scraper.email_notifier import send_email_notification
        
        if EMAIL_CONFIG["enabled"] and new_projects:
            try:
                # Pass empty list for todays_projects as it's no longer used
                send_email_notification(
                    new_projects, 
                    [],
                    EMAIL_CONFIG["sender_email"],
                    EMAIL_CONFIG["receiver_email"],
                    EMAIL_CONFIG["sender_password"]
                )
            except Exception as e:
                print(f"  ✗ Failed to send email: {e}")
        
        # Exit code based on results
        if new_projects:
            return 2  # New projects found
        return 0
    else:
        print("\n⚠ No projects found. The website structure may have changed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
