---
description: How to correctly add a new website scraper to the ProjectFinder system.
---

1.  **Analyze the Target Site**
    - Use the browser tool to navigate to the procurement portal URL.
    - Identify the list of projects and the selectors for each field (ID, Title, URL, Date).
    - Determine if the site is static or dynamic (requires JavaScript waiting).

2.  **Document Findings**
    - Create a new file `scraper/[name].md`.
    - Briefly describe the site's behavior and any discovered limitations.

3.  **Implement the Scraper Module**
    - Create `scraper/[name].py`.
    - Use `@register_scraper("[type]")` from `scraper.registry`.
    - Inherit from `BaseScraper`.
    - Implement `scrape_portal(self, portal_key, portal_config)`.
    - Use `self.browser.navigate(url)`, `self.browser.wait_for_element(...)`, and `self.browser.find_elements(...)`.
    - Ensure projects are returned as a list of `Project` dataclasses.

4.  **Register the Module**
    - Open `scraper/__init__.py`.
    - Add `from scraper import [name]` to the end of the file.

5.  **Configure the Portal**
    - Open `config.py`.
    - Add a new entry to the `PORTALS` dictionary using the unique `portal_key` and matching `type`.

6.  **Verify the Implementation**
    - Run the command: `python main.py` or `python run_scraper.py`.
    - Confirm that the new projects appear in the logs and `data/seen_projects.json`.
