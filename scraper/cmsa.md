# CMSA Bid Opportunities (PlanetBids)

The Central Marin Sanitation Agency (CMSA) uses a PlanetBids portal for its procurement opportunities.

### Details:
- **Base URL:** `https://www.cmsa.us/projects/bid-opportunities`
- **Portal URL:** `https://vendors.planetbids.com/portal/63909/bo/bo-search`
- **Type:** PlanetBids

### Table Structure:
- **Posted:** Date project was posted.
- **Project Title:** Title and description.
- **Invitation #:** Used as the unique project ID.
- **Due Date:** Closing date for the bid.

### Implementation Note:
This portal is handled by the `PlanetBidsScraper` in `scraper/planetbids.py`. The scraper uses the portal ID `63909` from the URL to construct detail links.
