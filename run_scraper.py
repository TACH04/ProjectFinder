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
# from scraper.email_notifier import send_email_notification  <-- Moved to local scope


# Import scrapers to ensure they are registered
import scraper.opengov
import scraper.bonfire_scraper
import scraper.chandler_scraper
import scraper.gilbert
import scraper.mesa_engineering
import scraper.glendale
import scraper.cave_creek
import scraper.maricopa
import scraper.planetbids
import scraper.petaluma

# Configure logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "scraper.log")

# Create a custom logger
logger = logging.getLogger("ProjectFinder")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Console handler with Unicode safety for Windows
class UnicodeSafeStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            super().emit(record)
        except UnicodeEncodeError:
            # Fallback for terminals that don't support emojis/UTF-8
            msg = self.format(record)
            # Replace non-encodable characters with '?'
            clean_msg = msg.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
            sys.stdout.write(clean_msg + self.terminator)
            self.flush()

console_handler = UnicodeSafeStreamHandler()
console_handler.setFormatter(logging.Formatter('%(message)s'))  # Keep console clean/simple
logger.addHandler(console_handler)


def generate_popup_notification(new_projects, all_projects, failed_portals=None):
    """
    Generate an HTML file with new projects and open it directly
    to serve as a 'popup' notification.
    """
    timestamp = datetime.now().strftime('%A, %B %d, %Y %I:%M %p')
    filename = "latest_projects.html"
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>ProjectFinder Alert</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; background-color: #f5f5f7; }}
            .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); overflow: hidden; }}
            .header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; }}
            .header h2 {{ margin: 0; font-size: 24px; }}
            .header p {{ margin: 5px 0 0; opacity: 0.8; font-size: 14px; }}
            .content {{ padding: 20px; }}
            .project-list {{ list-style: none; padding: 0; margin: 0; }}
            .project-item {{ padding: 15px 0; border-bottom: 1px solid #eee; display: grid; grid-template-columns: 200px 1fr; gap: 20px; align-items: start; }}
            .project-item:last-child {{ border-bottom: none; }}
            .city {{ font-weight: 600; color: #2c3e50; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }}
            .project-details {{ display: flex; flex-direction: column; gap: 4px; }}
            .project-name {{ color: #007aff; text-decoration: none; font-weight: 500; font-size: 16px; line-height: 1.4; }}
            .project-name:hover {{ text-decoration: underline; }}
            .project-id {{ font-size: 12px; color: #888; background: #f0f0f0; padding: 2px 6px; border-radius: 4px; }}
            .section-title {{ color: #2c3e50; border-bottom: 2px solid #e74c3c; padding-bottom: 8px; margin-bottom: 15px; font-size: 18px; }}
            .empty-state {{ text-align: center; color: #888; padding: 40px; font-style: italic; }}
            .footer {{ background: #f9f9f9; padding: 15px; text-align: center; font-size: 12px; color: #999; border-top: 1px solid #eee; }}
            .summary {{ margin-top: 20px; padding: 15px; background: #e8f4fd; border-radius: 8px; color: #2980b9; font-size: 14px; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>ProjectFinder Alert</h2>
                <p>{timestamp}</p>
            </div>
            
            <div class="content">
    """
    

    
    # Helper to get city name (reused logic from email_notifier essentially)
    def get_city_name(portal_key):
         # PORTALS is global in run_scraper
         if portal_key in PORTALS:
             return PORTALS[portal_key].get('name', portal_key.title())
         return portal_key.title()
    
    if new_projects:
        html += f"""
                <h3 class="section-title">🚨 New Projects ({len(new_projects)})</h3>
                <ul class="project-list">
        """

        for p in new_projects:
            city_name = get_city_name(p.portal)
            link_html = f'<a href="{p.url}" class="project-name" target="_blank">{p.title}</a>' if p.url else f'<span class="project-name">{p.title}</span>'
            
            html += f"""
                    <li class="project-item">
                        <div class="city">{city_name}</div>
                        <div class="project-details">
                            {link_html}
                            <span class="project-id">{p.id}</span>
                        </div>
                    </li>
            """
        html += "</ul>"
    else:
        html += '<div class="empty-state">No new projects found since last check.</div>'

    if failed_portals:
        html += f"""
                <h3 class="section-title" style="border-color: #f1c40f; margin-top: 30px;">⚠️ Skipped Portals ({len(failed_portals)})</h3>
                <ul class="project-list">
        """
        for p_key in failed_portals:
            city_name = get_city_name(p_key)
            html += f"""
                    <li class="project-item">
                        <div class="city" style="color: #e67e22;">{city_name}</div>
                        <div class="project-details">
                            <span class="project-name" style="color: #95a5a6;">Connection Failed / Timeout</span>
                            <span class="project-id">SKIPPED</span>
                        </div>
                    </li>
            """
        html += "</ul>"

    html += f"""
                <div class="summary">
                    Total Active Projects Scanned: <strong>{len(all_projects)}</strong>
                </div>
            </div>
            
            <div class="footer">
                Generated by ProjectFinder • <a href="file://{os.getcwd()}" style="color:#999">View Project Folder</a>
            </div>
        </div>
        
        <script>
            // Optional: Auto-close functionality or simple interactions could go here
        </script>
    </body>
    </html>
    """

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
            
        # Open the file
        if sys.platform == 'win32':
            os.startfile(filename)
        elif sys.platform == 'darwin':
            # Use 'open' to open in default browser
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
        "--portal",
        help="Optional: Run only this specific portal (e.g., 'arizona_app')"
    )
    parser.add_argument(
        "--validate", 
        action="store_true",
        help="Run in validation mode: scrape all, capture screenshots, generate report, DO NOT save."
    )
    parser.add_argument(
        "--ghost",
        action="store_true",
        help="Run in Ghost Mode (browser hidden/off-screen)"
    )
    parser.add_argument(
        "--reset-browser",
        action="store_true",
        help="Clear the browser profile to fix hanging/navigation issues"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    
    if getattr(args, 'reset_browser', False):
        import shutil
        profile_dir = os.path.join(os.path.dirname(__file__), ".chrome_profile")
        if os.path.exists(profile_dir):
            try:
                shutil.rmtree(profile_dir)
                print(f"🧹 Successfully cleared browser profile. Starting fresh!")
            except Exception as e:
                print(f"⚠ Failed to clear browser profile: {e}")
                if os.name == 'nt':
                    print("  Attempting to forcefully close stuck Chrome processes...")
                    try:
                        import subprocess
                        subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe', '/T'], capture_output=True)
                        subprocess.run(['taskkill', '/F', '/IM', 'chromedriver.exe', '/T'], capture_output=True)
                        time.sleep(1)
                        if os.path.exists(profile_dir):
                            shutil.rmtree(profile_dir)
                        print(f"🧹 Successfully cleared browser profile after killing stuck processes.")
                    except Exception as e2:
                        print(f"⚠ Still failed to clear: {e2}")
        else:
            print("✨ Browser profile is already clean.")
    
    logger.info(f"🚀 Starting Scraper Run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"   Notification Mode: {args.notify}")
    if args.ghost:
        logger.info("   👻 MODE: GHOST (Browser Hidden)")
    
    if args.validate:
        logger.info("   🔍 MODE: VALIDATION (Screenshots on, Saving off)")

    all_projects = []
    failed_portals = [] # Track portals that completely failed

    
    # Validation setup
    validation_dir = None
    screenshots = {}
    if args.validate:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        validation_dir = os.path.join("logs", f"validation_{timestamp}")
        os.makedirs(validation_dir, exist_ok=True)

    # 1. Scrape all portals
    try:
        # Ghost mode overrides default headless setting
        headless = args.ghost or BROWSER_SETTINGS["headless"]
        
        # We need to distinguish between scrapers that need the shared browser (OpenGov, Gilbert)
        # and those that can run in parallel (API-based or simple requests).
        # Currently, 'opengov' and 'gilbert' use the browser. 
        # 'bonfire' and 'chandler' use requests (though they can accept browser).
        
        browser_types = ["opengov", "gilbert", "mesa_engineering", "glendale", "cave_creek", "maricopa", "planetbids", "arizona_app", "petaluma"]

        # Validation mode uses its own profile to avoid lock conflicts
        user_data_dir = os.path.join(DATA_DIR, "validation_profile") if args.validate else None
        
        with StealthBrowser(headless=headless, user_data_dir=user_data_dir) as browser:
            
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

            # Filter portals if --portal is specified
            target_portals = PORTALS
            if getattr(args, 'portal', None):
                if args.portal in PORTALS:
                    target_portals = {args.portal: PORTALS[args.portal]}
                else:
                    logger.error(f"Portal '{args.portal}' not found in configuration.")
                    return 1

            for key, config in target_portals.items():
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
                            failed_portals.append(p_key) # Track failure
                    except Exception as e:
                        logger.error(f"  ✗ Unexpected error scraping {p_key}: {e}", exc_info=True)
                        failed_portals.append(p_key) # Track failure
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
                if not browser.is_healthy():
                    logger.warning(f"⚠ Browser is unhealthy before scraping {key}. Attempting restart...")
                    if not browser.restart():
                        logger.error(f"✗ Failed to restart browser. Skipping {key}.")
                        failed_portals.append(key)
                        continue

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
    # In validation mode, we check for curiosities but DO NOT save to seen_projects.json
    save_to_db = not args.validate
    new_projects, _ = check_for_new_projects(all_projects, save=save_to_db)

    # 3. Handle Notification & Report
    if args.validate:
        generate_validation_report(all_projects, screenshots, validation_dir)
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
        generate_popup_notification(new_projects, all_projects, failed_portals)
        
    else:
        # Email mode (Default)
        if new_projects or failed_portals:
            if not EMAIL_CONFIG["enabled"]:
                logger.info("📧 Email notifications disabled; skipping email send.")
            elif not EMAIL_CONFIG["sender_email"] or not EMAIL_CONFIG["receiver_email"]:
                logger.error("📧 Missing sender/receiver email in .env; skipping email send.")
            else:
                logger.info(f"📧 Sending email notification for {len(new_projects)} new projects...")
                try:
                    from scraper.email_notifier import send_email_notification
                    success = send_email_notification(
                        new_projects,
                        EMAIL_CONFIG["sender_email"],
                        EMAIL_CONFIG["receiver_email"],
                        failed_portals=failed_portals
                    )
                except ImportError:
                     logger.error("  ✗ Could not import email notifier (check dependencies).")
                     success = False

                if success:
                    logger.info("  ✓ Email notification sent successfully!")
                else:
                    logger.error("  ✗ Failed to send email notification.")
        else:
            logger.info("😴 No new projects or failures to notify about.")

    logger.info(f"✅ Run completed. Total Projects scanned: {len(all_projects)}")
    return 0


def capture_screenshots_scroll(browser, validation_dir, key):
    """
    Capture multiple screenshots by scrolling down the page.
    Returns a list of saved filenames.
    """
    filenames = []
    # We use a smaller scroll step than the viewport height to ensure overlap
    # and to account for any fixed headers we might fail to hide.
    # We use 500 for more overlap and to ensure elements at the edge are caught.
    scroll_step = 500 
    
    try:
        # 1. Provide a small buffer for heavy React apps to finish initial rendering
        time.sleep(2)

        # 2. Hide fixed elements (headers/footers/popups) that obscure content
        # This version is more careful to only hide true fixed/sticky headers
        browser.driver.execute_script("""
            document.querySelectorAll('*').forEach(el => {
                const style = window.getComputedStyle(el);
                const pos = style.position;
                const top = parseInt(style.top);
                const height = el.offsetHeight;
                
                // Hide elements that stay at the top or are explicitly fixed/sticky
                if (pos === 'fixed' || pos === 'sticky') {
                     // Check if it's a large overlay (likely a popup) or a header
                     if (top < 100 || height > window.innerHeight * 0.8) {
                        el.style.opacity = '0'; 
                        el.style.pointerEvents = 'none';
                     }
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
            
            current_scroll += (scroll_step - 50) # 50px overlap
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
