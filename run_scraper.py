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
import concurrent.futures

from config import PORTALS, BROWSER_SETTINGS, DATA_DIR, EMAIL_CONFIG
from scraper.browser import StealthBrowser
from scraper.base import PortalScrapingError
from scraper.registry import get_scraper_class
from scraper.notifications import check_for_new_projects, notify_new_projects
from scraper.email_notifier import send_email_notification

# Import scrapers to ensure they are registered
import scraper.opengov
import scraper.bonfire_scraper
import scraper.chandler_scraper
import scraper.gilbert
import scraper.mesa_engineering

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
    parser.add_argument(
        "--validate", 
        action="store_true",
        help="Run in validation mode: scrape all, capture screenshots, generate report, DO NOT save."
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    
    logger.info(f"🚀 Starting Scraper Run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"   Notification Mode: {args.notify}")
    if args.validate:
        logger.info("   🔍 MODE: VALIDATION (Screenshots on, Saving off)")

    all_projects = []
    
    # Validation setup
    validation_dir = None
    screenshots = {}
    if args.validate:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        validation_dir = os.path.join("logs", f"validation_{timestamp}")
        os.makedirs(validation_dir, exist_ok=True)

    # 1. Scrape all portals
    try:
        headless = BROWSER_SETTINGS["headless"]
        
        # We need to distinguish between scrapers that need the shared browser (OpenGov, Gilbert)
        # and those that can run in parallel (API-based or simple requests).
        # Currently, 'opengov' and 'gilbert' use the browser. 
        # 'bonfire' and 'chandler' use requests (though they can accept browser).
        
        browser_types = ["opengov", "gilbert", "mesa_engineering", "glendale", "cave_creek"]

        with StealthBrowser(headless=headless) as browser:
            
            # Dictionary to hold reusable scraper instances
            # Some scrapers might be stateful or heavy to init, so we instantiate once per type
            scraper_instances = {}

            def get_or_create_scraper(p_type):
                if p_type not in scraper_instances:
                    scraper_cls = get_scraper_class(p_type)
                    if not scraper_cls:
                        logger.error(f"Unknown scraper type: {p_type}")
                        return None
                    # Pass specific browser instance
                    scraper_instances[p_type] = scraper_cls(browser) 
                return scraper_instances[p_type]

            # Separate portals
            browser_portals = {}
            api_portals = {}

            for key, config in PORTALS.items():
                p_type = config.get("type", "opengov")
                if p_type in browser_types:
                    browser_portals[key] = config
                else:
                    api_portals[key] = config

            # Helper function for scraping a single portal safely
            def scrape_single_portal(p_key, p_config):
                p_type = p_config.get("type", "opengov")
                scraper = get_or_create_scraper(p_type)
                
                if not scraper:
                    return []

                # Retry logic
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        logger.info(f"Reading portal: {p_config['name']} ({p_key})")
                        projects = scraper.scrape_portal(p_key, p_config)
                        logger.info(f"  ✓ Found {len(projects)} active projects for {p_key}")
                        return projects
                    except PortalScrapingError as e:
                        if attempt < max_retries - 1:
                            wait_time = (attempt + 1) * 5
                            logger.warning(f"  ⚠ Attempt {attempt+1} failed ({e}). Retrying in {wait_time}s...")
                            time.sleep(wait_time)
                        else:
                            logger.error(f"  ✗ All {max_retries} attempts failed for {p_key}: {e}")
                    except Exception as e:
                        logger.error(f"  ✗ Unexpected error scraping {p_key}: {e}", exc_info=True)
                        break
                return []

            # 1. Run API scrapers in PARALLEL
            # Note: We must ensure get_or_create_scraper is thread safe or pre-create instances
            # Since we are using a shared 'scraper_instances' dict, we should pre-create them OR lock.
            # But actually, 'bonfire' and 'chandler' scrapers don't strictly *need* the shared browser object 
            # for their requests logic, but we pass it anyway. 
            # Requests is thread safe.
            
            # Let's pre-create instances for API portals to avoid race conditions in get_or_create
            for _, config in api_portals.items():
                get_or_create_scraper(config.get("type", "opengov"))

            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                future_to_portal = {
                    executor.submit(scrape_single_portal, key, config): key 
                    for key, config in api_portals.items()
                }
                
                for future in concurrent.futures.as_completed(future_to_portal):
                    p_key = future_to_portal[future]
                    try:
                        results = future.result()
                        all_projects.extend(results)
                    except Exception as e:
                        logger.error(f"API Scraper thread failed for {p_key}: {e}")

            # 2. Run Browser scrapers SEQUENTIALLY (Browser is not thread-safe)
            for key, config in browser_portals.items():
                results = scrape_single_portal(key, config)
                all_projects.extend(results)
                
                # Capture screenshot for validation
                if args.validate:
                    try:
                        time.sleep(1) # Wait for initial render
                        images = capture_screenshots_scroll(browser, validation_dir, key)
                        if images:
                            screenshots[key] = images
                            logger.info(f"  📸 Screenshots saved for {key}: {len(images)} images")
                    except Exception as e:
                        logger.error(f"  ✗ Screenshot failed for {key}: {e}")

            # 3. IF VALIDATION: Screenshot API portals
            if args.validate:
                logger.info("--------------------------------------------------")
                logger.info("📸 Capturing screenshots for API portals...")
                
                # We reuse the existing browser instance
                for key, config in api_portals.items():
                    try:
                        url = config.get('url')
                        if not url:
                            continue
                            
                        logger.info(f"  Navigating to {key} ({url})...")
                        if browser.navigate(url):
                             time.sleep(2) # Give it time to render fully
                             images = capture_screenshots_scroll(browser, validation_dir, key)
                             if images:
                                 screenshots[key] = images
                                 logger.info(f"  ✓ Screenshots saved for {key}: {len(images)} images")
                        else:
                             logger.error(f"  ✗ Failed to navigate to {key}")
                    except Exception as e:
                        logger.error(f"  ✗ API Screenshot failed for {key}: {e}")

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
    if args.validate:
        generate_validation_report(all_projects, screenshots, validation_dir)
        # Check for new projects but DO NOT SAVE
        new_projects, _ = check_for_new_projects(all_projects, save=False)
        logger.info(f"🔎 Validation: Found {len(all_projects)} active projects ({len(new_projects)} new).")
        logger.info(f"📄 Report generated at: {os.path.join(validation_dir, 'index.html')}")
        
        # Open the report
        report_path = os.path.join(validation_dir, "index.html")
        try:
            if sys.platform == 'win32':
                os.startfile(report_path)
            elif sys.platform == 'darwin':
                subprocess.call(('open', report_path))
            else:
                subprocess.call(('xdg-open', report_path))
        except Exception:
            pass
            
        return 0

    if args.notify == "popup":
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


def capture_screenshots_scroll(browser, validation_dir, key):
    """
    Capture multiple screenshots by scrolling down the page.
    Returns a list of saved filenames.
    """
    filenames = []
    # We use a smaller scroll step than the viewport height to ensure overlap
    # and to account for any fixed headers we might fail to hide.
    scroll_step = 600 
    
    try:
        # 1. Hide fixed elements (headers/footers/popups) that obscure content
        # This prevents them from appearing in every screenshot and blocking the "middle"
        browser.driver.execute_script("""
            var style = document.createElement('style');
            style.innerHTML = '* { position: static !important; }'; 
            // The above is too aggressive, might break layout. 
            // Better to just hide fixed/sticky elements:
            document.querySelectorAll('*').forEach(el => {
                var pos = window.getComputedStyle(el).position;
                if (pos === 'fixed' || pos === 'sticky') {
                    el.style.visibility = 'hidden'; 
                    // or el.style.display = 'none'; 
                    // visibility hidden preserves layout space which is safer
                }
            });
        """)
        time.sleep(0.5)

        # Get total height
        total_height = browser.driver.execute_script("return document.body.scrollHeight")
        current_scroll = 0
        index = 1
        
        # Max captures to avoid infinite loops on infinite scroll pages
        # Increased to 20 for long pages like Mesa Engineering
        max_captures = 20
        
        while current_scroll < total_height and index <= max_captures:
            # Scroll to position
            browser.driver.execute_script(f"window.scrollTo(0, {current_scroll});")
            time.sleep(1.0) # Wait for render/lazy-load
            
            # Capture
            filename = f"{key}_{index}.png"
            path = os.path.join(validation_dir, filename)
            browser.driver.save_screenshot(path)
            filenames.append(filename)
            logger.info(f"  📸 Captured part {index}: {filename}")
            
            current_scroll += scroll_step
            index += 1
            
        return filenames

    except Exception as e:
        logger.error(f"  ✗ Screenshot capture error: {e}")
        return filenames


def generate_validation_report(all_projects, screenshots_map, output_dir):
    """
    Generate an HTML report for validation
    screenshots_map: { 'portal_key': ['img1.png', 'img2.png'] }
    """
    projects_by_portal = {}
    for p in all_projects:
        if p.portal not in projects_by_portal:
            projects_by_portal[p.portal] = []
        projects_by_portal[p.portal].append(p)

    html = [
        "<html><head><title>ProjectFinder Validation Report</title>",
        "<style>",
        "body { font-family: sans-serif; padding: 20px; background: #f0f0f0; }",
        ".portal-card { background: white; margin-bottom: 30px; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); display: flex; gap: 20px; }",
        ".screenshot-col { flex: 0 0 400px; display: flex; flex-direction: column; gap: 10px; }",
        ".screenshot-wrapper { width: 100%; border: 1px solid #ddd; border-radius: 4px; overflow: hidden; position: relative; }",
        ".screenshot-wrapper img { width: 100%; display: block; cursor: pointer; transition: transform 0.2s; }",
        ".screenshot-wrapper img:hover { transform: scale(1.5); box-shadow: 0 10px 20px rgba(0,0,0,0.2); z-index: 10; position: relative; }",
        ".projects { flex: 1; }",
        "h2 { margin-top: 0; color: #333; }",
        "ul { list-style: none; padding: 0; }",
        "li { padding: 8px 0; border-bottom: 1px solid #eee; }",
        ".count { font-weight: bold; color: #666; font-size: 0.9em; }",
        ".id { font-family: monospace; background: #eee; padding: 2px 5px; border-radius: 3px; font-size: 0.9em; color: #555; }",
        "</style></head><body>",
        f"<h1>ProjectFinder Validation Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}</h1>",
        f"<p>Found {len(all_projects)} total projects across {len(screenshots_map)} scanned portals.</p>"
    ]

    # Sort by portal name
    for portal_key in sorted(screenshots_map.keys()):
        images = screenshots_map.get(portal_key, [])
        projects = projects_by_portal.get(portal_key, [])
        
        html.append(f'<div class="portal-card">')
        
        # Screenshot Column
        html.append(f'<div class="screenshot-col">')
        if images:
            for img_file in images:
                html.append(f'<div class="screenshot-wrapper"><a href="{img_file}" target="_blank"><img src="{img_file}" title="Click to open full size"></a></div>')
        else:
            html.append('<div style="background:#eee;height:200px;display:flex;align-items:center;justify-content:center;color:#999;">No Screenshot</div>')
        html.append('</div>')
        
        # Projects Column
        html.append(f'<div class="projects">')
        html.append(f'<h2>{portal_key} <span class="count">({len(projects)} projects)</span></h2>')
        
        if projects:
            html.append('<ul>')
            for p in projects:
                link_html = f'<a href="{p.url}" target="_blank">View</a>' if p.url else ''
                html.append(f'<li><span class="id">{p.id}</span> <strong>{p.title}</strong> {link_html}</li>')
            html.append('</ul>')
        else:
            html.append('<p><em>No active projects found.</em></p>')
            
        html.append('</div></div>')

    html.append("</body></html>")
    
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(html))


if __name__ == "__main__":
    sys.exit(main())
