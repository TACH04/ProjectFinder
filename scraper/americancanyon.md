# City of American Canyon (OpenGov)

The City of American Canyon uses an OpenGov Procurement portal for its bid opportunities.

### Details:
- **Base URL:** `https://www.cityofamericancanyon.org/government/finance/doing-business-with-the-city/bids-and-requests-for-proposals`
- **Portal URL:** `https://procurement.opengov.com/portal/cityofamericancanyon`
- **Type:** OpenGov

### Table Structure:
- **Release Date:** When the project was published.
- **Project Title:** The name of the bid opportunity.
- **ID:** The OpenGov internal project ID (e.g., 12345).

### Implementation Note:
This portal is handled by the generic `OpenGovScraper` in `scraper/opengov.py`. The scraper automatically sorts by release date and extracts project titles and IDs.
