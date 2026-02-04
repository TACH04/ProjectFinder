# Setting Up the Daily Scheduler

This guide explains how to set up ProjectFinder to run automatically every morning at 7:00 AM.

## Windows Setup

The Windows scheduler installs a Task Scheduler job that runs in the background.

### Installation
1. Navigate to the `scheduler` folder in the project directory.
2. Right-click on **`install_schedule_windows.bat`**.
3. Select **"Run as Administrator"**.
   - *Note: Administrator privileges are required to create scheduled tasks.*
4. A terminal window will open and confirm:
   > `✅ Scheduler installed!`
   > `Runs daily at 7:00 AM`
5. Press any key to close the window.

### Managing the Scheduler (Windows)
Open **Command Prompt** or **PowerShell** to run these commands:

- **Check Status**:
  ```cmd
  schtasks /query /tn "ProjectFinder Daily Check"
  ```
- **Run Manually**:
  ```cmd
  schtasks /run /tn "ProjectFinder Daily Check"
  ```
- **Uninstall**:
  ```cmd
  schtasks /delete /tn "ProjectFinder Daily Check" /f
  ```

---

## macOS Setup

The macOS scheduler uses `launchd` to run the script in the background.

### Installation
1. Open your **Terminal**.
2. Navigate to the project folder, then the scheduler folder:
   ```bash
   cd /path/to/ProjectFinder/scheduler
   ```
3. Run the installer script:
   ```bash
   ./install_schedule_mac.sh
   ```
4. You should see:
   > `✅ Scheduler installed!`
   > `Runs daily at 7:00 AM`

### Managing the Scheduler (macOS)
Run these commands in your **Terminal**:

- **Check Status**:
  ```bash
  launchctl list | grep projectfinder
  ```
  *(If you see a line starting with a number or `-`, it is installed)*

- **Run Manually**:
  ```bash
  launchctl start com.projectfinder.daily
  ```

- **Uninstall**:
  ```bash
  launchctl unload ~/Library/LaunchAgents/com.projectfinder.daily.plist
  rm ~/Library/LaunchAgents/com.projectfinder.daily.plist
  ```

## Logs
Both schedulers verify their runs by writing to the `logs/` folder in your project directory:
- `logs/scraper.log`: Standard output (success messages, projects found)
- `logs/scraper_error.log`: Error messages (crashes, connection issues)

## Troubleshooting & FAQ
**Q: Will it run if my computer is asleep?**
- **Windows**: No, standard tasks do not wake the computer unless explicitly configured.
- **macOS**: No, it will not wake your computer. However, if the 7:00 AM time is missed while asleep, it will run immediately when you next wake the computer.
