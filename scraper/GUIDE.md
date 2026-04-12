# Guide: Adding a New Scraper

This guide outlines the process for integrating a new procurement portal into the ProjectFinder system.

## Workflow Overview

1.  **Research**: Analyze the target website's DOM and navigation flow.
2.  **Analysis Document**: Create a `scraper/[name].md` file to record selectors and findings.
3.  **Implementation**: Create a `scraper/[name].py` file and implement the scraper class.
4.  **Registration**: Add the new module to `scraper/__init__.py`.
5.  **Configuration**: Add the portal details to `PORTALS` in `config.py`.
6.  **Verification**: Test the scraper using `run_scraper.py`.

---

## Step 1: Research & Analysis

Use the browser tools to identify:
- **Project List Page**: The URL where projects are listed.
- **Row Selectors**: The CSS selector that identifies each project in the list (e.g., `tr`, `div.project-card`).
- **Data Points**: Selectors for ID, Title, Release Date, and Detail URL.
- **Dynamic Content**: Does the site use React/Vue (needs Selenium waits) or is it static HTML?

Create a file named `scraper/[portal_name].md` and document any quirks (e.g., "only returns 15 results per page", "requires scrolling").

---

## Step 2: Implementation

Create `scraper/[portal_name].py`. Follow this template:

```python
from typing import List, Optional
from selenium.webdriver.common.by import By
from scraper.base import BaseScraper, Project, PortalScrapingError
from scraper.registry import register_scraper
from datetime import datetime

@register_scraper("portal_type_name")
class MyNewScraper(BaseScraper):
    def scrape_portal(self, portal_key: str, portal_config: dict) -> List[Project]:
        url = portal_config["url"]
        
        # 1. Navigate
        if not self.browser.navigate(url):
            raise PortalScrapingError(f"Failed to navigate to {url}")
        
        # 2. Wait for elements
        self.browser.wait_for_element(By.CSS_SELECTOR, ".project-row", timeout=20)
        
        # 3. Extract
        return self._extract_projects(portal_key)

    def _extract_projects(self, portal_key: str) -> List[Project]:
        projects = []
        rows = self.browser.find_elements(By.CSS_SELECTOR, ".project-row")
        for row in rows:
            # Parse logic here
            # title = row.find_element(...).text
            # projects.append(Project(id=..., title=title, portal=portal_key, ...))
            pass
        return projects
```

### Key Considerations

- **Registration**: The string in `@register_scraper("name")` must match the `type` field in `config.py`.
- **Browser Protocol**: Use `self.browser` which provides a safe wrapper for Selenium operations.
- **Error Handling**: Raise `PortalScrapingError` for fatal issues; catch and log non-fatal row parsing errors.
- **Dates**: Use `datetime.strptime` or regex to parse dates. If no date is found, use `datetime.now()`.

---

## Step 3: Registration

Open `scraper/__init__.py` and add your new module to the imports:

```python
# scraper/__init__.py
from scraper import ..., my_new_scraper
```

---

## Step 4: Configuration

Open `config.py` and add an entry to the `PORTALS` dictionary:

```python
# config.py
PORTALS = {
    ...
    "my_portal_key": {
        "name": "Friendly Display Name",
        "url": "https://example.com/bids",
        "type": "portal_type_name"  # Matches @register_scraper
    },
}
```

---

## Step 5: Verification

Run the manual scraper script to test your implementation:

```bash
python main.py
```

Check the logs or `data/seen_projects.json` to see if your new projects are being captured correctly.
