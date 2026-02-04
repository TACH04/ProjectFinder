"""
Configuration for OpenGov Procurement Scraper
"""

# Portal configurations - add more portals as needed
PORTALS = {
    "phoenix": {
        "name": "City of Phoenix",
        "url": "https://procurement.opengov.com/portal/phoenix",
    },
    "surpriseaz": {
        "name": "City of Surprise, AZ", 
        "url": "https://procurement.opengov.com/portal/surpriseaz",
    },
}

# Browser settings
BROWSER_SETTINGS = {
    "headless": False,  # Set to True for background operation (may reduce bypass success)
    "wait_timeout": 30,  # Seconds to wait for page elements
    "cloudflare_wait": 30,  # Max seconds to wait for Cloudflare bypass
}

# Data storage
DATA_DIR = "data"
SEEN_PROJECTS_FILE = "data/seen_projects.json"
