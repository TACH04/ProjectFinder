
import os
import sys
import subprocess
import getpass
from datetime import datetime

PLIST_NAME = "com.projectfinder.daily"
TASK_NAME = "ProjectFinder Daily Check"

def get_project_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def is_mac():
    return sys.platform == "darwin"

def is_windows():
    return sys.platform == "win32"

def get_scheduler_status():
    if is_mac():
        plist_path = os.path.expanduser(f"~/Library/LaunchAgents/{PLIST_NAME}.plist")
        if os.path.exists(plist_path):
            try:
                result = subprocess.run(["launchctl", "list"], capture_output=True, text=True)
                if PLIST_NAME in result.stdout:
                    return "Enabled"
                return "Installed (Disabled)"
            except:
                return "Installed"
        return "Not Installed"
    elif is_windows():
        try:
            result = subprocess.run(["schtasks", "/query", "/tn", TASK_NAME], capture_output=True, text=True)
            if TASK_NAME in result.stdout:
                return "Enabled"
            return "Not Installed"
        except:
            return "Not Installed"
    return "Unsupported OS"

def install_scheduler(hour, minute):
    project_dir = get_project_dir()
    python_exe = os.path.join(project_dir, ".venv", "bin", "python3") if is_mac() else os.path.join(project_dir, ".venv", "Scripts", "python.exe")
    script_path = os.path.join(project_dir, "run_scraper.py")
    
    if is_mac():
        plist_path = os.path.expanduser(f"~/Library/LaunchAgents/{PLIST_NAME}.plist")
        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{PLIST_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_exe}</string>
        <string>{script_path}</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{project_dir}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>{hour}</integer>
        <key>Minute</key>
        <integer>{minute}</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>{project_dir}/logs/scraper.log</string>
    <key>StandardErrorPath</key>
    <string>{project_dir}/logs/scraper_error.log</string>
</dict>
</plist>"""
        with open(plist_path, "w") as f:
            f.write(plist_content)
        
        subprocess.run(["launchctl", "unload", plist_path], capture_output=True)
        result = subprocess.run(["launchctl", "load", plist_path], capture_output=True, text=True)
        if result.returncode == 0:
            return True, f"Scheduled for {hour:02d}:{minute:02d} daily."
        return False, result.stderr

    elif is_windows():
        time_str = f"{hour:02d}:{minute:02d}"
        cmd = [
            "schtasks", "/create", "/tn", TASK_NAME, 
            "/tr", f'"{python_exe}" "{script_path}"', 
            "/sc", "daily", "/st", time_str, "/f"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return True, f"Scheduled for {time_str} daily."
        return False, result.stderr

    return False, "Unsupported OS"

def uninstall_scheduler():
    if is_mac():
        plist_path = os.path.expanduser(f"~/Library/LaunchAgents/{PLIST_NAME}.plist")
        subprocess.run(["launchctl", "unload", plist_path], capture_output=True)
        if os.path.exists(plist_path):
            os.remove(plist_path)
        return True, "Scheduler removed."
    elif is_windows():
        result = subprocess.run(["schtasks", "/delete", "/tn", TASK_NAME, "/f"], capture_output=True, text=True)
        if result.returncode == 0:
            return True, "Scheduler removed."
        return False, result.stderr
    return False, "Unsupported OS"
