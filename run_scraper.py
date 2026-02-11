#!/usr/bin/env python3
"""
Production script for ProjectFinder
Scrapes projects and emails ONLY if new projects are detected.
"""

import os
import sys
import logging
import time
import argparse
import subprocess
from datetime import datetime

from config import PORTALS, BROWSER_SETTINGS, DATA_DIR, EMAIL_CONFIG
from scraper.browser import StealthBrowser
from scraper.scraper import OpenGovScraper, PortalScrapingError
from scraper.bonfire_scraper import BonfireScraper
from scraper.notifications import check_for_new_projects, notify_new_projects
from scraper.email_notifier import send_email_notification

# Configure logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "scraper.log")

# Create a custom logger
logger = logging.getLogger("ProjectFinder")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(message)s'))  # Keep console clean/simple
logger.addHandler(console_handler)


def generate_popup_notification(new_projects, all_projects):
    """
    Generate a text file with new projects and open it directly
    to serve as a 'popup' notification.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = "latest_projects.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("📋 PROJECT FINDER ALERTS\n")
        f.write(f"Checked at: {timestamp}\n")
        f.write("=" * 60 + "\n\n")
        
        if new_projects:
            f.write(f"🚨 FOUND {len(new_projects)} NEW PROJECTS:\n")
            f.write("-" * 40 + "\n")
            for p in new_projects:
                f.write(f"• [{p.portal}] {p.title}\n")
                if p.url:
                    f.write(f"  Link: {p.url}\n")
                f.write("\n")
        else:
            f.write("✓ No new projects found since last check.\n")
            
        f.write("\n" + "=" * 60 + "\n")
        f.write(f"Total Active Projects Scanned: {len(all_projects)}\n")

    # Open the file with default application
    try:
        if sys.platform == 'win32':
            os.startfile(filename)
        elif sys.platform == 'darwin':
            subprocess.call(('open', filename))
        else:
            subprocess.call(('xdg-open', filename))
        logger.info(f"  ✓ Popup notification opened: {filename}")
        return True
    except Exception as e:
        logger.error(f"  ✗ Failed to open popup file: {e}")
        return False


def parse_arguments():
    parser = argparse.ArgumentParser(description="Run ProjectFinder Scraper")
    parser.add_argument(
        "--notify", 
        choices=["email", "popup"], 
        default="email",
        help="Notification method: 'email' (default) or 'popup' (opens text file)"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    
    logger.info(f"🚀 Starting Scraper Run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"   Notification Mode: {args.notify}")

    all_projects = []

    # 1. Scrape all portals
    try:
        headless = BROWSER_SETTINGS["headless"]

        # Only initialize browser if we have OpenGov portals (or others needing it)
        # But for simplicity, we keep the structure.
        # We can pass browser to BonfireScraper too (it ignores it or uses it as fallback)
        
        with StealthBrowser(headless=headless) as browser:
            opengov_scraper = OpenGovScraper(browser)
            bonfire_scraper = BonfireScraper(browser)


            for portal_key, portal_config in PORTALS.items():
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        logger.info(f"Reading portal: {portal_config['name']} ({portal_key})")
                        
                        portal_type = portal_config.get("type", "opengov")
                        if portal_type == "bonfire":
                            projects = bonfire_scraper.scrape_portal(portal_key, portal_config)
                        else:
                            projects = opengov_scraper.scrape_portal(portal_key, portal_config)
                            
                        logger.info(f"  ✓ Found {len(projects)} active projects for {portal_key}")
                        all_projects.extend(projects)
                        break  # Success, exit retry loop
                    except PortalScrapingError as e:
                        if attempt < max_retries - 1:
                            wait_time = (attempt + 1) * 30  # 30s, 60s wait
                            logger.warning(f"  ⚠ Attempt {attempt+1} failed ({e}). Retrying in {wait_time}s...")
                            time.sleep(wait_time)
                        else:
                            logger.error(f"  ✗ All {max_retries} attempts failed for {portal_key}: {e}")
                    except Exception as e:
                        logger.error(f"  ✗ Unexpected error scraping {portal_key}: {e}", exc_info=True)
                        break  # Don't retry unexpected errors

    except Exception as e:
        logger.error(f"✗ Browser/Scraper validation error: {e}", exc_info=True)
        return 1

    if not all_projects:
        logger.warning("⚠ No active projects found on any portal.")
        return 0

    # 2. Check for new projects
    logger.info("🔍 Checking for new projects against database...")
    new_projects, _ = check_for_new_projects(all_projects)

    # 3. Print CLI summary
    if new_projects:
        logger.info(f"Found {len(new_projects)} NEW projects.")
        for p in new_projects:
            logger.info(f"  + New: {p.title} ({p.portal})")
    else:
        logger.info("No new projects found.")

    # 4. Handle Notification
    if args.notify == "popup":
        # Always generate popup if mode is popup, even if no new projects (to confirm run)
        # OR should we only popup if new? The request says "get the output as a pop-up notes file"
        # usually manual runs expect feedback.
        # But if we automate it via scheduler with popup flag? No, scheduler is typically email.
        # Let's fallback to: if new projects -> popup. If not -> maybe just log?
        # "My client wants the option to run the scraper manually ... and get the output as a pop-up notes file"
        # If I run manually, I want to know it finished.
        # I'll generate the file regardless, showing "No new projects" if empty.
        logger.info("📝 Generating popup notification...")
        generate_popup_notification(new_projects, all_projects)
        
    else:
        # Email mode (Default)
        if new_projects:
            if not EMAIL_CONFIG["enabled"]:
                logger.info("📧 Email notifications disabled; skipping email send.")
            elif not EMAIL_CONFIG["sender_email"] or not EMAIL_CONFIG["receiver_email"]:
                logger.error("📧 Missing sender/receiver email in .env; skipping email send.")
            else:
                logger.info(f"📧 Sending email notification for {len(new_projects)} new projects...")
                success = send_email_notification(
                    new_projects,
                    all_projects,
                    EMAIL_CONFIG["sender_email"],
                    EMAIL_CONFIG["receiver_email"],
                )

                if success:
                    logger.info("  ✓ Email notification sent successfully!")
                else:
                    logger.error("  ✗ Failed to send email notification.")
        else:
            logger.info("😴 No new projects to notify about.")

    logger.info("✅ Run completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
