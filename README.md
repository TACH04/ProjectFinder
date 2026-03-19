# ProjectFinder

An automated procurement scraper designed to monitor government portals and alert users to new project releases. It provides a centralized dashboard for tracking OpenGov, Bonfire, and municipal portals.

<img src="projectfindericon.png" alt="ProjectFinder Header" width="400">

## Overview

ProjectFinder automates the tedious process of manual portal checking. It uses stealth browser automation to navigate municipal and regional procurement sites, identifies new postings, and delivers structured reports via email or desktop notifications.

## Key Features

- **Multi-Portal Support**: Unified scraping logic for OpenGov, Bonfire, and custom municipal platforms.
- **Stealth Automation**: Built with `undetected-chromedriver` to minimize detection on platforms protected by Cloudflare.
- **Flexible Notifications**: HTML email reports (via Gmail/OAuth2) or local desktop summaries.
- **Integrated Scheduler**: Automated run management for macOS (LaunchAgents) and Windows (Task Scheduler).
- **Validation Mode**: Diagnostic tool for capturing screenshots and generating verification reports.

## Quick Start

### 1. Prerequisites
- **Python 3.11+**
- **Google Chrome**

### 2. Installation
```bash
git clone https://github.com/TACH04/ProjectFinder.git
cd ProjectFinder
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Usage

#### Terminal Interface (Recommended)
Launch the interactive dashboard to manage settings, schedules, and manual runs:
```bash
python3 interface.py
```

#### Command Line Interface
For automation or power users, run the core scraper directly:
```bash
python3 run_scraper.py --notify [email|popup] [--ghost] [--validate]
```

---

## Architecture

ProjectFinder is built with an extensible, object-oriented design:

- **Core Engine**: `run_scraper.py` manages the orchestration of browser sessions and data persistence.
- **Base Scraper**: `scraper/base.py` provides the blueprint for all scrapers, handling common tasks like navigation and element detection.
- **Specialized Scrapers**: Modular components in `scraper/` tailored for specific portal types:
  - `OpenGovScraper`: Modern procurement portals.
  - `BonfireScraper`: Regional municipal platforms.
  - `Custom Scrapers`: Targeted logic for sites like Glendale, Chandler, and Maricopa County.

### Extensibility: Adding New Portals
The project is designed to scale. To add a new portal:
1. Inherit from `BaseScraper` in a new file within `scraper/`.
2. Implement the `scrape()` method using the provided `StealthBrowser` instance.
3. Register the portal in `config.py`.

---

## Configuration

### Notifications
ProjectFinder supports OAuth2 for secure email delivery.
1. Run `interface.py` and navigate to **Settings > Setup Emailer**.
2. Provide a recipient email and follow the automated OAuth flow to authorize your sender Gmail account.
3. If `credentials.json` is missing, the application will provide a setup guide.

### Ghost Mode
Enable **Ghost Mode** to run the scraper in a small, non-intrusive window. The browser is automatically positioned off-screen, allowing for background execution without the performance overhead of traditional headless modes (which are easily detected).

---

## Troubleshooting

- **Browser Detection**: If a site is blocked by Cloudflare, try running in visible mode (Ghost Mode OFF) to solve the initial captcha manually.
- **OAuth Failures**: Ensure `credentials.json` is placed in the project root and configured as a "Desktop App" in the Google Cloud Console.
- **Dependencies**: Reinstall requirements if you encounter import errors: `pip install -U -r requirements.txt`.

---
*Developed for efficient procurement monitoring and government project tracking.*
