# PlanetBids Scraper

The PlanetBids scraper identifies project information from vendor portals.

### Behavior:
- **Project Capture:** Extracts basic project metadata including ID, Title, and Detail URL.
- **30-Project Limit:** The scraper currently captures the first 30 projects (the most recent entries). This provides sufficient coverage for recent bidding opportunities, as archived projects are often years old.

### Technical Note:
The extraction focuses on the initial batch of results provided by the portal.