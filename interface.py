
#!/usr/bin/env python3
import os
import sys
import json
import subprocess
from datetime import datetime
import scheduler.manage_schedule as scheduler_manager

SETTINGS_FILE = "user_settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {"notification_type": "email"}

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 50)
    print("        PROJECT FINDER CLIENT INTERFACE")
    print("=" * 50)
    settings = load_settings()
    notif = settings.get("notification_type", "email").upper()
    sched = scheduler_manager.get_scheduler_status()
    print(f" Notification: {notif} | Scheduler: {sched}")
    print("-" * 50)

def run_scraper(validate=False):
    settings = load_settings()
    notif_type = settings.get("notification_type", "email")
    
    cmd = [sys.executable, "run_scraper.py", "--notify", notif_type]
    if validate:
        cmd.append("--validate")
        print("\n🔍 Running in VALIDATION mode (Screenshots enabled, Saving disabled)...")
    else:
        print(f"\n🚀 Running Scraper (Notification: {notif_type})...")
    
    try:
        subprocess.run(cmd)
    except Exception as e:
        print(f"❌ Error running scraper: {e}")
    
    input("\nPress Enter to return to menu...")

def change_notification():
    settings = load_settings()
    current = settings.get("notification_type", "email")
    new_type = "popup" if current == "email" else "email"
    settings["notification_type"] = new_type
    save_settings(settings)
    print(f"\n✅ Notification type changed to: {new_type.upper()}")
    import time
    time.sleep(1)

def check_updates():
    print("\n📩 Checking for updates from GitHub...")
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"❌ Error checking updates: {e}")
    
    input("\nPress Enter to return to menu...")

def manage_scheduler():
    while True:
        clear_screen()
        print_header()
        print("1. Install/Update Scheduler")
        print("2. Uninstall/Disable Scheduler")
        print("3. Back to Main Menu")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            time_input = input("\nEnter run time (HH:MM, default 07:00): ") or "07:00"
            try:
                hour, minute = map(int, time_input.split(":"))
                success, msg = scheduler_manager.install_scheduler(hour, minute)
                if success:
                    print(f"\n✅ {msg}")
                else:
                    print(f"\n❌ Failed: {msg}")
            except ValueError:
                print("\n❌ Invalid time format. Use HH:MM (e.g., 08:30).")
            input("\nPress Enter to continue...")
        elif choice == "2":
            success, msg = scheduler_manager.uninstall_scheduler()
            if success:
                print(f"\n✅ {msg}")
            else:
                print(f"\n❌ Failed: {msg}")
            input("\nPress Enter to continue...")
        elif choice == "3":
            break

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("1. RUN SCRAPER (Default)")
        print("2. CHANGE NOTIFICATION TYPE")
        print("3. RUN VALIDATION MODE")
        print("4. CHECK FOR UPDATES")
        print("5. MANAGE SCHEDULER")
        print("6. EXIT")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            run_scraper()
        elif choice == "2":
            change_notification()
        elif choice == "3":
            run_scraper(validate=True)
        elif choice == "4":
            check_updates()
        elif choice == "5":
            manage_scheduler()
        elif choice == "6":
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main_menu()
