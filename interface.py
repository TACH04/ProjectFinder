#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.layout import Layout
from rich.align import Align
import select
import scheduler.manage_schedule as scheduler_manager

# Configuration
SETTINGS_FILE = "user_settings.json"
console = Console()

def load_settings():
    """Load user settings from JSON file."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)
            # Ensure defaults
            if "notification_type" not in settings: settings["notification_type"] = "email"
            if "ghost_mode" not in settings: settings["ghost_mode"] = False
            return settings
    return {"notification_type": "email", "ghost_mode": False}

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

def run_scraper(validate=False):
    """Run the scraper script."""
    settings = load_settings()
    notif_type = settings.get("notification_type", "email")
    ghost_mode = settings.get("ghost_mode", False)
    
    cmd = [sys.executable, "run_scraper.py", "--notify", notif_type]
    
    if ghost_mode:
        cmd.append("--ghost")

    console.print()
    if validate:
        cmd.append("--validate")
        console.print(Panel("[bold yellow]Running in VALIDATION mode[/bold yellow]\nScreenshots enabled, Database saving disabled.", border_style="yellow"))
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
                console.print("[bold green]✅ You are up to date![/bold green]")
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
[3] Back to Main Menu"""
        
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

def main_menu():
    """Display the main menu."""
    # Check updates silently on startup (and auto-apply if found)
    with console.status("[bold blue]Checking for updates...[/bold blue]", spinner="dots", spinner_style="magenta"):
        check_updates(auto=True)
        # If updated, it will restart, so we won't reach here if an update occurred.
        update_available = False # We can assume false if we are still running


    first_run = True  # Track if this is the first menu display
    
    while True:
        clear_screen()
        console.print(get_header_panel())
        
        # Auto-update handles notification/restart, so we don't need to show a panel here anymore.


        menu_text = """[bold white]1.[/bold white] RUN SCRAPER [dim](Default)[/dim]
[bold white]2.[/bold white] CHANGE NOTIFICATION TYPE
[bold white]3.[/bold white] TOGGLE GHOST MODE
[bold white]4.[/bold white] RUN VALIDATION MODE
[bold white]5.[/bold white] CHECK FOR UPDATES
[bold white]6.[/bold white] MANAGE SCHEDULER
[bold white]7.[/bold white] EXIT"""

        console.print(Panel(menu_text, title="Main Menu", border_style="blue", expand=False))
        
        # Timeout logic for default option
        choice = None
        
        # Countdown loop - only on first menu display
        try:
            if first_run and os.name != 'nt':
                for i in range(5, 0, -1):
                    console.print(f"[dim]Auto-running in {i} seconds... (Press Enter to run immediately)[/dim]", end="\r")
                    rlist, _, _ = select.select([sys.stdin], [], [], 1)
                    if rlist:
                        user_input = sys.stdin.readline().strip()
                        choice = user_input if user_input else "1"
                        break
                # Clear the countdown line
                console.print(" " * 80, end="\r")
            else:
                # Windows fallback or subsequent runs - no auto-run
                choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6", "7"], default="1")

        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting...[/bold red]")
            sys.exit(0)
        
        # If no input after countdown, auto-run and exit
        if choice is None:
            run_scraper()
        elif choice == "1":
            run_scraper()
            first_run = False  # Disable auto-run for subsequent menu displays
        elif choice == "2":
            change_notification()
            first_run = False
        elif choice == "3":
            change_ghost_mode()
            first_run = False
        elif choice == "4":
            run_scraper(validate=True)
            first_run = False
        elif choice == "5":
            check_updates()
            first_run = False
        elif choice == "6":
            manage_scheduler()
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
