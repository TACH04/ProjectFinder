# ProjectFinder 🕵️‍♂️

A modern, automated procurement scraper designed to help you find and bid on government projects before anyone else. It monitors OpenGov portals and alerts you the moment a new project is released.

![ProjectFinder Header](projectfindericon.png)

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.11+**
- **Google Chrome** (The scraper uses it to navigate portals)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/TACH04/ProjectFinder.git
cd ProjectFinder

# Install dependencies
pip install -r requirements.txt
```

### 3. Launch
- **macOS/Linux**: `python3 interface.py`
- **Windows**: Double-click `run_manual.bat` (or run `python interface.py`)

---

## 🖥️ The Dashboard

ProjectFinder features a beautiful terminal-based interface (TUI) to manage your operations without touching a line of code.

- **[1] Run Scraper**: Start a fresh search across all configured portals.
- **[2] Notification Type**: Toggle between **Email Alerts** and **Popup Summaries**.
- **[3] Ghost Mode**: Toggle between **Visible** and **Hidden** browser sessions.
- **[4] Validation Mode**: Run a diagnostic check (captures screenshots, doesn't save to database).
- **[5] Settings**: Access update checks, email setup, and scheduler management.

---

## 🔔 Notifications

### Email Alerts (Recommended)
Sends a clean HTML report directly to your inbox.
1. Go to **Settings > Setup Emailer**.
2. Enter your recipient email.
3. Follow the automated OAuth flow to authorize your sender Gmail account.
   - *Note: If `credentials.json` is missing, a setup guide will open automatically.*

### Popup Summaries
Displays a quick summary of new projects in a text window on your desktop. Perfect for manual runs.

---

## 👻 Ghost Mode
Tired of browser windows popping up? Toggle **Ghost Mode** ON to run the scraper silently in a hidden window. It automatically moves the browser off-screen so you can keep working uninterrupted.

---

## 📅 Daily Scheduler
Never miss a project again. Use the built-in **Scheduler Management** (under Settings) to set ProjectFinder to run automatically every morning (e.g., at 7:00 AM).

- **Windows**: Installs as a Background Task in Task Scheduler.
- **macOS**: Installs as a LaunchAgent.

---

## 🧪 Validation Mode
Want to see what the scraper is seeing? **Validation Mode** runs the scraper visibly, takes screenshots of every portal results page, and generates a detailed report in the `logs/` folder. It **won't** save these projects to your "seen" database, making it perfect for testing.

---

## 🛠️ Advanced Usage (CLI)

For power users or custom scripts, you can run the core scraper directly:

```bash
python3 run_scraper.py --notify [email|popup] [--ghost] [--validate] [--portal PORTAL_NAME]
```

---

## ❓ Troubleshooting

- **"python is not recognized"**: Ensure Python is added to your system's PATH.
- **Browser Crashes**: Make sure you have the latest version of Google Chrome installed.
- **Cloudflare Blocks**: If a site stays on "Just a moment...", ProjectFinder will wait for you to solve the captcha manually.
- **OAuth Errors**: Ensure your `credentials.json` is placed in the project root and is of type "Desktop App".

---

*Built with ❤️ for procurement professionals.*
