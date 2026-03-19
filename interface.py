#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import time
import shutil
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.layout import Layout
from rich.align import Align
import select
import scheduler.manage_schedule as scheduler_manager
import setup_email_oauth

# Configuration
SETTINGS_FILE = "user_settings.json"
ENV_FILE = ".env"
SEEN_PROJECTS_FILE = os.path.join("data", "seen_projects.json")
LOGS_DIR = "logs"

console = Console()

def load_settings():
    """Load user settings from JSON file."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            try:
                settings = json.load(f)
            except json.JSONDecodeError:
                settings = {}
            
            # Ensure defaults
            if "notification_type" not in settings: settings["notification_type"] = "email"
            if "ghost_mode" not in settings: settings["ghost_mode"] = False
            if "auto_run_timer" not in settings: settings["auto_run_timer"] = 5
            return settings
    return {"notification_type": "email", "ghost_mode": False, "auto_run_timer": 5}

def save_settings(settings):
    """Save user settings to JSON file."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def clear_screen():
    """Clear the terminal screen."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

def get_header_panel():
    """Create the header panel."""
    settings = load_settings()
    notif = settings.get("notification_type", "email").upper()
    ghost = "ON" if settings.get("ghost_mode", False) else "OFF"
    sched = scheduler_manager.get_scheduler_status()
    
    # Compact info line
    info = f"[magenta]Notification:[/magenta] {notif} | [magenta]Ghost Mode:[/magenta] {ghost} | [magenta]Scheduler:[/magenta] {sched}"
    
    return Panel(
        Align.center(info),
        title="[bold blue]PROJECT FINDER[/bold blue]",
        subtitle="[italic white]State Procurement Scraper[/italic white]",
        border_style="blue",
        expand=False,
        padding=(0, 2)
    )

def run_scraper(validate=False, reset_browser=False):
    """Run the scraper script."""
    settings = load_settings()
    notif_type = settings.get("notification_type", "email")
    ghost_mode = settings.get("ghost_mode", False)
    
    cmd = [sys.executable, "run_scraper.py", "--notify", notif_type]
    
    if ghost_mode and not validate:
        cmd.append("--ghost")
        
    if reset_browser:
        cmd.append("--reset-browser")

    console.print()
    if validate:
        cmd.append("--validate")
        console.print(Panel("[bold yellow]Running in VALIDATION mode[/bold yellow]\nScreenshots enabled, Database saving disabled.\n[italic]Ghost Mode bypassed (Browser Visible)[/italic]", border_style="yellow"))
    elif reset_browser:
        console.print(Panel(f"[bold red]Running Scraper (RESET BROWSER)[/bold red]\nClearing `.chrome_profile` before starting...", border_style="red"))
    else:
        mode_str = "GHOST (Hidden)" if ghost_mode else "VISIBLE"
        console.print(Panel(f"[bold blue]Running Scraper[/bold blue]\nNotification: [magenta]{notif_type}[/magenta] | Mode: [magenta]{mode_str}[/magenta]", border_style="blue"))
    
    try:
        # Run subprocess and stream output
        with console.status("[bold blue]Scraping in progress...[/bold blue]", spinner="dots", spinner_style="magenta"):
             subprocess.run(cmd)
        pass
    except Exception as e:
        console.print(f"[bold red]❌ Error running scraper:[/bold red] {e}")
    
    # Always exit after scraper completes
    console.print("\n[bold green]✓ Run complete. Exiting.[/bold green]")
    time.sleep(1)
    sys.exit(0)

def change_notification():
    """Toggle notification settings."""
    settings = load_settings()
    current = settings.get("notification_type", "email")
    new_type = "popup" if current == "email" else "email"
    settings["notification_type"] = new_type
    save_settings(settings)
    
    console.print(f"\n[bold green]✅ Notification type changed to:[/bold green] [magenta]{new_type.upper()}[/magenta]")
    time.sleep(1.5)

def change_ghost_mode():
    """Toggle ghost mode settings."""
    settings = load_settings()
    current = settings.get("ghost_mode", False)
    new_mode = not current
    settings["ghost_mode"] = new_mode
    save_settings(settings)
    
    status = "ON (Hidden)" if new_mode else "OFF (Visible)"
    console.print(f"\n[bold green]👻 Ghost Mode changed to:[/bold green] [magenta]{status}[/magenta]")
    time.sleep(1.5)

def configure_auto_run():
    """Configure the auto-run countdown timer."""
    settings = load_settings()
    current_timer = settings.get("auto_run_timer", 5)
    
    if current_timer == 0:
        console.print(f"\n[bold]Current Auto-Run Timer:[/bold] [bold red]Auto-run turned off[/bold red]")
    else:
        console.print(f"\n[bold]Current Auto-Run Timer:[/bold] {current_timer} seconds")
    new_timer = IntPrompt.ask("Enter new timer duration in seconds ([bold magenta]0[/bold magenta] to turn off)", default=current_timer)
    
    settings["auto_run_timer"] = new_timer
    save_settings(settings)
    if new_timer == 0:
        console.print(f"\n[bold green]✅ Auto-run turned off.[/bold green]")
    else:
        console.print(f"\n[bold green]✅ Auto-Run timer set to {new_timer} seconds.[/bold green]")
    time.sleep(1.5)

def setup_emailer():
    """Setup email notifications and OAuth."""
    console.print("\n[bold blue]📧 Email Notification Setup[/bold blue]")
    
    # 1. Ask for Receiver Email
    current_receiver = ""
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            for line in f:
                if line.startswith("RECEIVER_EMAIL="):
                    current_receiver = line.strip().split("=", 1)[1]
                    break
    
    receiver_email = Prompt.ask("\nEnter the email address to receive notifications", default=current_receiver)
    
    # Update .env
    env_content = []
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            env_content = f.readlines()
    
    # Remove existing RECEIVER_EMAIL line
    env_content = [line for line in env_content if not line.startswith("RECEIVER_EMAIL=")]
    # Add new one
    env_content.append(f"RECEIVER_EMAIL={receiver_email}\n")
    # Ensure EMAIL_ENABLED is true
    env_content = [line for line in env_content if not line.startswith("EMAIL_ENABLED=")]
    env_content.insert(0, "EMAIL_ENABLED=true\n")

    with open(ENV_FILE, "w") as f:
        f.writelines(env_content)
    
    console.print("\n[bold green]✅ Recipient email saved.[/bold green]")
    
    # 2. Check/Setup OAuth
    if Confirm.ask("\nDo you want to configure the sender email (Gmail OAuth)?"):
        if os.path.exists("credentials.json"):
            console.print("\n[dim]Found credentials.json, starting authentication...[/dim]")
            try:
                setup_email_oauth.authenticate_gmail()
                console.print("\n[bold green]✅ OAuth Authentication Successful! Token saved.[/bold green]")
            except Exception as e:
                console.print(f"\n[bold red]❌ Authentication failed:[/bold red] {e}")
        else:
            console.print("\n[bold yellow]⚠️  credentials.json NOT FOUND[/bold yellow]")
            console.print("Opening setup guide in your browser...")
            import webbrowser
            guide_path = os.path.abspath("email_setup_guide.html")
            webbrowser.open(f"file://{guide_path}")
            console.print("\n[dim]Follow the instructions in the browser window to get your credentials.json file.[/dim]")
            console.print("Once you have the file, run this setup again.")
            
    time.sleep(2)

def clear_logs():
    """Delete all log files and folders."""
    if Confirm.ask("\nAre you sure you want to DELETE ALL LOGS (including screenshots & validation reports)?"):
        if os.path.exists(LOGS_DIR):
            for filename in os.listdir(LOGS_DIR):
                file_path = os.path.join(LOGS_DIR, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    console.print(f"[red]Error deleting {filename}: {e}[/red]")
            console.print("\n[bold green]✅ Logs and artifacts cleared.[/bold green]")
        else:
            console.print("\n[dim]No logs directory found.[/dim]")
    time.sleep(1.5)

def clear_seen_projects():
    """Reset the seen_projects.json file."""
    console.print("\n[bold red]⚠️  WARNING: This will make the scraper re-notify you about ALL existing projects![/bold red]")
    if Confirm.ask("Are you sure you want to RESET the seen projects database?"):
        try:
            with open(SEEN_PROJECTS_FILE, "w") as f:
                json.dump({"projects": {}}, f, indent=2)
            console.print("\n[bold green]✅ Project database reset.[/bold green]")
        except Exception as e:
            console.print(f"\n[bold red]❌ Error resetting database:[/bold red] {e}")
    time.sleep(1.5)
            

def check_update_status():
    """Check if updates are available (updates local remote info)."""
    try:
        subprocess.run(["git", "fetch"], check=True, capture_output=True)
        status = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True).stdout
        if "Your branch is behind" in status:
            return True
    except Exception:
        pass
    return False

def check_updates(auto=False):
    """Check for updates. if auto=True, pull and restart without prompt."""
    if not auto:
        console.print("\n[bold blue]📩 Checking for updates from GitHub...[/bold blue]")
    
    try:
        if check_update_status():
            if auto:
                console.print(Panel("[bold magenta]🚀 Update Available! Installing...[/bold magenta]", border_style="magenta"))
                subprocess.run(["git", "pull"], check=True)
                console.print("[bold green]✅ Updated successfully! Restarting...[/bold green]")
                time.sleep(1)
                # Restart the script
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                console.print(Panel("[bold magenta]⚠ Update Available![/bold magenta]\nYour local version is behind the remote repository.", border_style="magenta"))
                if Confirm.ask("Do you want to pull updates now?"):
                    subprocess.run(["git", "pull"], check=True)
                    console.print("[bold green]✅ Updated successfully! Restarting...[/bold green]")
                    time.sleep(1)
                    os.execv(sys.executable, [sys.executable] + sys.argv)
                    return True # Updated (though we restart, so this might not be reached)
        else:
            if not auto:
                console.print("\n[bold green]✅ You are up to date![/bold green]")
    except Exception as e:
        if not auto:
            console.print(f"[bold red]❌ Error checking updates:[/bold red] {e}")
    
    if not auto:
        console.input("\n[dim]Press Enter to return to menu...[/dim]")
    return False

def manage_scheduler():
    """Sub-menu for scheduler management."""
    while True:
        clear_screen()
        console.print(get_header_panel())
        
        menu = """[1] Install/Update Scheduler
[2] Uninstall/Disable Scheduler
[3] Back"""
        
        console.print(Panel(menu, title="Scheduler Management", border_style="blue"))
        
        choice = Prompt.ask("Select an option", choices=["1", "2", "3"])
        
        if choice == "1":
            time_input = Prompt.ask("Enter run time (HH:MM)", default="07:00")
            try:
                hour, minute = map(int, time_input.split(":"))
                success, msg = scheduler_manager.install_scheduler(hour, minute)
                if success:
                    console.print(f"\n[bold green]✅ {msg}[/bold green]")
                else:
                    console.print(f"\n[bold red]❌ Failed:[/bold red] {msg}")
            except ValueError:
                console.print("\n[bold red]❌ Invalid time format.[/bold red]")
            console.input("\n[dim]Press Enter to continue...[/dim]")
            
        elif choice == "2":
            success, msg = scheduler_manager.uninstall_scheduler()
            if success:
                console.print(f"\n[bold green]✅ {msg}[/bold green]")
            else:
                console.print(f"\n[bold red]❌ Failed:[/bold red] {msg}")
            console.input("\n[dim]Press Enter to continue...[/dim]")
            
        elif choice == "3":
            break

def settings_menu():
    """Sub-menu for settings and maintenance."""
    while True:
        clear_screen()
        console.print(get_header_panel())

        menu_text = """[bold white]1.[/bold white] Check for Updates
[bold white]2.[/bold white] Configure Auto-Run Timer
[bold white]3.[/bold white] Setup Emailer
[bold white]4.[/bold white] Manage Scheduler
[bold white]5.[/bold white] Clear Logs
[bold white]6.[/bold white] Clear Seen Projects
[bold white]7.[/bold white] Back to Main Menu"""

        console.print(Panel(menu_text, title="Settings & Maintenance", border_style="blue", expand=False))

        choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6", "7"])

        if choice == "1":
            check_updates()
        elif choice == "2":
            configure_auto_run()
        elif choice == "3":
            setup_emailer()
        elif choice == "4":
            manage_scheduler()
        elif choice == "5":
            clear_logs()
        elif choice == "6":
            clear_seen_projects()
        elif choice == "7":
            break

def main_menu():
    """Display the main menu."""
    # Check updates silently on startup (and auto-apply if found)
    with console.status("[bold blue]Checking for updates...[/bold blue]", spinner="dots", spinner_style="magenta"):
        # Suppress output during silent check unless update found
        check_updates(auto=True)

    first_run = True  # Track if this is the first menu display
    
    while True:
        clear_screen()
        console.print(get_header_panel())
        
        menu_text = """[bold white]1.[/bold white] RUN SCRAPER [dim](Default)[/dim]
[bold white]2.[/bold white] TOGGLE GHOST MODE
[bold white]3.[/bold white] CHANGE NOTIFICATION TYPE
[bold white]4.[/bold white] RUN VALIDATION MODE
[bold white]5.[/bold white] RESET BROWSER [dim](Fixes Hangs)[/dim]
[bold white]6.[/bold white] SETTINGS
[bold white]7.[/bold white] EXIT"""

        console.print(Panel(menu_text, title="Main Menu", border_style="blue", expand=False))
        
        # Timeout logic for default option
        choice = None
        
        # Countdown loop - only on first menu display
        try:
            settings = load_settings()
            timer_seconds = settings.get("auto_run_timer", 5)

            if first_run and os.name != 'nt' and timer_seconds > 0:
                for i in range(timer_seconds, 0, -1):
                    console.print(f"[dim]Auto-running in {i} seconds... (Press Enter to run immediately)[/dim]", end="\r")
                    rlist, _, _ = select.select([sys.stdin], [], [], 1)
                    if rlist:
                        user_input = sys.stdin.readline().strip()
                        choice = user_input if user_input else "1"
                        break
                
                # If we finished the loop without setting choice, we should auto-run (choice "1")
                if choice is None:
                    choice = "1"
                    
                # Clear the countdown line
                console.print(" " * 80, end="\r")
            
        # Windows fallback or subsequent runs
            if choice is None:
                choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6", "7"], default="1")

        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting...[/bold red]")
            sys.exit(0)
        

        if choice == "1":
            run_scraper()
            first_run = False
        elif choice == "2":
            change_ghost_mode()
            first_run = False
        elif choice == "3":
            change_notification()
            first_run = False
        elif choice == "4":
            run_scraper(validate=True)
            first_run = False
        elif choice == "5":
            if Confirm.ask("\nThis will clear the background browser profile to fix freezing. Continue?"):
                run_scraper(reset_browser=True)
            first_run = False
        elif choice == "6":
            settings_menu()
            first_run = False
        elif choice == "7":
            console.print("\n[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting...[/bold red]")
        sys.exit(0)
