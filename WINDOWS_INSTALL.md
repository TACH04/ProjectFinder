# Windows Manual Installation Guide

Follow these steps on your client's laptop to set up ProjectFinder. This will ensure `git pull` updates work and the "Click to Run" experience is smooth.

## 1. Install Prerequisites

### A. Python
1.  Download Python 3.11+ from [python.org](https://www.python.org/downloads/).
2.  Run the installer.
3.  **CRITICAL:** Check the box **"Add python.exe to PATH"** at the bottom of the first screen.
4.  Click "Install Now".

### B. Git
1.  Download Git for Windows from [git-scm.com](https://git-scm.com/download/win).
2.  Run the installer.
3.  Click "Next" through all the default options (the defaults are fine).

### C. Google Chrome
1.  Ensure Google Chrome is installed (the scraper uses it).

## 2. Set Up the Project

1.  **Open PowerShell** or Command Prompt.
2.  Navigate to where you want the project (e.g., Desktop):
    ```powershell
    cd Desktop
    ```
3.  **Clone the Repository**:
    ```powershell
    git clone https://github.com/TACH04/ProjectFinder.git
    ```
4.  **Enter the folder**:
    ```powershell
    cd ProjectFinder
    ```
5.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```

## 3. Create the "One-Click" Launcher

Since the client isn't technical, we'll create a simple file on the Desktop they can double-click.

### Option A: Create a `.bat` file (Easiest)
1.  Open Notepad.
2.  Paste the following code:
    ```batch
    @echo off
    cd /d "%~dp0"
    python interface.py
    pause
    ```
3.  Save the file **inside the `ProjectFinder` folder** as `run_app.bat`.
    *   *Make sure to select "All Files" in the "Save as type" dropdown so it doesn't become `run_app.bat.txt`.*

### Option B: Create a Desktop Shortcut
1.  Right-click `run_app.bat` (the file you just created options above).
2.  Select **"Send to" > "Desktop (create shortcut)"**.
3.  Rename the shortcut on the Desktop to "ProjectFinder".
4.  (Optional) Right-click the shortcut > Properties > Change Icon > Select the `icon.ico` if you have one.

## 4. First Run Verification

1.  Double-click the "ProjectFinder" shortcut.
2.  The interface should open.
3.  Select option **[5] CHECK FOR SCALER UPDATES** to test the git connection.
4.  Select option **[1] RUN SCRAPER** to test a quick scrape.

## Troubleshooting

-   **"python is not recognized"**: You missed the "Add to PATH" checkbox. Reinstall Python or add it to system environment variables manually.
-   **"git is not recognized"**: Restart the command prompt/PowerShell after installing Git.
-   **Browser crashes**: Ensure Chrome is up to date.
-   **Cloudflare Check**: If the script pauses at "Just a moment...", you may need to manually click the "Verify you are human" checkbox. The script will wait 60 seconds for you to do this.
