import os
from dotenv import load_dotenv

load_dotenv()

# Portal configurations - add more portals as needed
PORTALS = {
    "phoenix": {
        "name": "City of Phoenix",
        "url": "https://procurement.opengov.com/portal/phoenix",
        "type": "opengov"
    },
    "surpriseaz": {
        "name": "City of Surprise, AZ", 
        "url": "https://procurement.opengov.com/portal/surpriseaz",
        "type": "opengov"
    },
    "sedona": {
        "name": "City of Sedona",
        "url": "https://sedonaaz.bonfirehub.com/portal/?tab=openOpportunities",
        "type": "bonfire"
    },
    # New OpenGov Targets
    "tollesonaz": {
        "name": "City of Tolleson",
        "url": "https://procurement.opengov.com/portal/tollesonaz",
        "type": "opengov"
    },
    "elmirageaz": {
        "name": "City of El Mirage",
        "url": "https://procurement.opengov.com/portal/elmirageaz",
        "type": "opengov"
    },
    "tucsonaz": {
        "name": "City of Tucson",
        "url": "https://procurement.opengov.com/portal/tucson-az",
        "type": "opengov"
    },
    "queencreekaz": {
        "name": "Town of Queen Creek",
        "url": "https://procurement.opengov.com/portal/queencreekaz",
        "type": "opengov"
    },
    # New Bonfire Targets
    "buckeyeaz": {
        "name": "City of Buckeye",
        "url": "https://buckeyeaz.bonfirehub.com/portal/?tab=openOpportunities",
        "type": "bonfire"
    },
    "goodyearaz": {
        "name": "City of Goodyear",
        "url": "https://goodyearaz.bonfirehub.com/portal/?tab=openOpportunities",
        "type": "bonfire"
    },
    "scottsdaleaz": {
        "name": "City of Scottsdale",
        "url": "https://scottsdaleaz.bonfirehub.com/portal/?tab=openOpportunities",
        "type": "bonfire"
    },
    "peoriaaz": {
        "name": "City of Peoria",
        "url": "https://peoriaaz.bonfirehub.com/portal/?tab=openOpportunities",
        "type": "bonfire"
    },
    "tempe": {
        "name": "City of Tempe",
        "url": "https://tempe-gov.bonfirehub.com/portal/?tab=openOpportunities",
        "type": "bonfire"
    },
}

# Browser settings
BROWSER_SETTINGS = {
    "headless": False,  # Set to True for background operation (may reduce bypass success)
    "wait_timeout": 30,  # Seconds to wait for page elements
    "cloudflare_wait": 30,  # Max seconds to wait for Cloudflare bypass
}

# Notification settings
EMAIL_CONFIG = {
    "enabled": os.getenv("EMAIL_ENABLED", "false").lower() == "true",
    "sender_email": os.getenv("SENDER_EMAIL", ""),
    "sender_password": os.getenv("SENDER_PASSWORD", ""),
    "receiver_email": os.getenv("RECEIVER_EMAIL", ""),
}

# Data storage
DATA_DIR = "data"
SEEN_PROJECTS_FILE = "data/seen_projects.json"
