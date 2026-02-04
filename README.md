# ProjectFinder

A targeted web scraper that detects **new** government procurement projects from OpenGov portals and sends email notifications.

## 🚀 Features
- **Smart Detection**: Ignores old projects; only alerts you about *freshly released* ones (using `run_scraper.py`).
- **Targeted Scraping**: Filters for "Active" projects and "Release Date" to ensure relevance.
- **Robust Bypassing**: Uses `undetected-chromedriver` and smart logic (e.g., waiting for specific React components) to handle Cloudflare and dynamic site content.
- **Email Alerts**: Sends clean, minimal HTML emails via Gmail API.
- **Automated**: Includes setup scripts for daily scheduling on macOS and Windows.

## 🛠️ Setup

1.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**
    Create a `.env` file with your details:
    ```env
    EMAIL_ENABLED=true
    SENDER_EMAIL=your-gmail@gmail.com
    RECEIVER_EMAIL=your-email@example.com
    ```
    *(Note: `SENDER_PASSWORD` is legacy/unused if using OAuth credentials below)*

3.  **Gmail OAuth Setup**
    -   Download `credentials.json` from Google Cloud Console (Desktop App type).
    -   Run `python3 setup_email_oauth.py` to generate `token.json`.

## 🏃 Usage

### 1. Automated Run (Recommended)
**Use this for cron jobs / schedulers.**
It runs strictly in headless mode and **only** notifies if *new* projects are found.
```bash
python3 run_scraper.py
```

### 2. Manual / Debug Run
**Use this for testing or forcing a check.**
Allows specific portal selection and visible browser mode.
```bash
# Check all portals (shows all output)
python3 main.py

# Check a specific portal
python3 main.py --portal phoenix

# Run visibly (not headless) for debugging
python3 main.py --headless
```

### 3. Dry Run (Simulated)
Checks for projects from the last 7 days (ignoring "seen" history).
```bash
python3 dry_run.py
```

## 📅 Scheduling

**Mac**
```bash
./scheduler/install_schedule_mac.sh
```

**Windows**
Run `scheduler\install_schedule_windows.bat` as Administrator.

## 🧪 Testing
Verify the notification logic without scraping:
```bash
python3 test_notifications.py
```

## 📂 Project Structure
-   `scraper/`: Core logic (browser, scraper, notifications).
-   `data/`: Stores `seen_projects.json` database.
-   `logs/`: Log files from scheduled runs.
-   `config.py`: Portal URLs and browser settings.
