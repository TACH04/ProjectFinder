The Arizona APP scraper has been upgraded to handle pagination and 30-day date filtering.

### Features:
- **Automatic Sorting:** Automatically sorts the portal by 'Begin Date' descending to ensure the most recent projects are processed first.
- **Pagination:** Traverses multiple pages (up to 20) until the date cutoff is reached.
- **30-Day Cutoff:** Intelligently stops scraping once it encounters projects older than 30 days, optimizing performance.
- **Robust Detection:** Uses icon-based detection (`fa-sort-down`) to verify sort order, bypassing deceptive `aria-label` behaviors.

### Performance:
In a typical run, it captures ~40-50 projects over 3-4 pages, providing much better coverage than the previous 15-project limit.