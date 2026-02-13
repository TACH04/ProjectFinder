
import time
import re
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraper.browser import StealthBrowser
from scraper.base import Project

def _extract_from_page_source(browser, portal_key: str):
    """Fallback: extract project data from raw page source"""
    projects = []
    source = browser.get_page_source()
    
    # Look for JSON object patterns common in OpenGov
    # DEBUG: Print snippets to see what we're working with
    print("Page source length:", len(source))
        
    # Look for JSON object patterns common in OpenGov
    # Pattern 1: {"id":12345,"title":"..."} or {"id":12345,..."title":"..."}
    # We enforce strict proximity (e.g. within 600 chars) to ensure we don't cross object boundaries
    # We use . instead of [^}] because there might be nested objects (like "template":{...}) between title and id
    patterns = [
        # Title ... ID (Allows alphanumeric IDs with dashes/spaces)
        r'"title"\s*:\s*"([^"]+)".{0,600}?"id"\s*:\s*"([^"]+)"',
        # ID ... Title
        r'"id"\s*:\s*"([^"]+)".{0,600}?"title"\s*:\s*"([^"]+)"',
            # Alternative format with 'jobTitle'
        r'"id"\s*:\s*"([^"]+)".{0,600}?"jobTitle"\s*:\s*"([^"]+)"',
        # Numeric ID specific patterns (just in case)
        r'"id"\s*:\s*(\d+).{0,600}?"title"\s*:\s*"([^"]+)"',
    ]
    
    seen_ids = set()
    
    for pattern in patterns:
        matches = re.findall(pattern, source)
        for match in matches:
            # Handle tuple unpacking based on which group is which
            if pattern.startswith(r'"title"'):
                title, pid = match
            else:
                pid, title = match
                
            if pid in seen_ids:
                continue
            
            # Check for "department" ID (common false positive)
            # Look at the text immediately preceding the ID match in the source
            # If we see "department":{"id":, then it's a department, not a project
            start_index = source.find(f'"id":{pid}')
            if start_index == -1:
                start_index = source.find(f'"id": {pid}')
            
            if start_index > 0:
                    preceding_text = source[max(0, start_index-20):start_index]
                    if '"department":{' in preceding_text or '"department": {' in preceding_text:
                        continue
                
            # Basic validation
            if len(title) < 3 or len(pid) < 3:
                continue
                
            # Check if it looks like a project (has status)
            # This is a heuristic to avoid random other IDs
            if '"status":' not in source[source.find(pid):source.find(pid)+500]:
                    # If we can't verify it's a project, skip generic small IDs
                    if len(pid) < 4: continue

            seen_ids.add(pid)
            
            url = f"https://procurement.opengov.com/portal/{portal_key}/projects/{pid}"
            
            projects.append(Project(
                id=pid,
                title=title,
                portal=portal_key,
                url=url,
                release_date=datetime.now(), # Fallback date
            ))
    
    return projects

def run():
    with StealthBrowser(headless=True) as browser:
        try:
            url = "https://procurement.opengov.com/portal/phoenix"
            print(f"Navigating to {url}...")
            start_time = time.time()
            browser.navigate(url)
            
            # Wait for meaningful content
            WebDriverWait(browser.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='row']"))
            )
            print(f"Page loaded in {time.time() - start_time:.2f}s")
            
            rows = browser.find_elements(By.XPATH, "//div[@role='row']")
            print(f"Found {len(rows)} rows.")
            if rows:
                print("First row HTML:")
                print(rows[0].get_attribute("outerHTML"))
            
            extract_start = time.time()

            projects = _extract_from_page_source(browser, "phoenix")
            print(f"Extraction took {time.time() - extract_start:.2f}s")
            print(f"Found {len(projects)} projects:")
            for p in projects[:5]:
                print(f"  - {p.title} ({p.id})")
                
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    run()
