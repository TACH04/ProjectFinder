# City of Petaluma Bid Opportunities Scraper

## Overview
Scraper for `https://cityofpetaluma.org/bid-opportunities-2/`.

## Behavior
- The site lists bids in several sections: "Current Bid Opportunities", "Current RFP Opportunities", and "Current RFQ Opportunities".
- Each item is a link to a detail page (e.g., `https://cityofpetaluma.org/documents/...`).
- The scraper visits each detail page to extract the **Published Date** and full **Title**.
- Project IDs are generated as a hash of the URL to ensure uniqueness.

## Selectors
- **Section Headers**: `h2` containing key terms.
- **Project Links**: `h3 a` or `li a` depending on the section widget.
- **Detail Page Date**: Container with date text (usually absolute positioned or in a specific grid).
- **Detail Page Title**: `h1` or similar main header.

## Limitations
- **Closing Dates**: Not extracted from PDFs in this version.
- **Deep Search**: Requires individual page loads for each project, making it slower than list-only scrapers.
