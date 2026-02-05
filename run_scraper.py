#!/usr/bin/env python3
"""
Production script for ProjectFinder
Scrapes projects and emails ONLY if new projects are detected.
"""

import os
import sys
import logging
from datetime import datetime

from config import PORTALS, BROWSER_SETTINGS, DATA_DIR, EMAIL_CONFIG
from scraper.browser import StealthBrowser
from scraper.scraper import OpenGovScraper
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


def main():
    logger.info(f"🚀 Starting Scraper Run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    all_projects = []

    # 1. Scrape all portals
    try:
        headless = BROWSER_SETTINGS["headless"]

        with StealthBrowser(headless=headless) as browser:
            scraper = OpenGovScraper(browser)

            for portal_key, portal_config in PORTALS.items():
                try:
                    logger.info(f"Reading portal: {portal_config['name']} ({portal_key})")
                    projects = scraper.scrape_portal(portal_key, portal_config)
                    logger.info(f"  ✓ Found {len(projects)} active projects for {portal_key}")
                    all_projects.extend(projects)
                except Exception as e:
                    logger.error(f"  ✗ Error scraping {portal_key}: {e}", exc_info=True)
                    continue

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

    # 4. Send Email if there are new projects
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
