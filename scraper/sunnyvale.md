# City of Sunnyvale (PlanetBids)

This portal uses the standard PlanetBids scraper.

### Details:
- **Agency:** City of Sunnyvale
- **Portal URL:** `https://vendors.planetbids.com/portal/75302/bo/bo-search`
- **Scraper Type:** `planetbids`

### Behavior:
- The portal displays a list of active bid opportunities.
- Each row in the table corresponds to a project.
- Scraping captures the project ID, title, and release date.
- Detail URLs are constructed using the `rowattribute` (internal ID) from the table.

### Known Limitations:
- **Lazy Loading:** The portal currently only shows up to 30 projects per run. While the total count may be higher (e.g., 38), the current scraper captures the most recent 30 projects, which is acceptable for the initial version.
