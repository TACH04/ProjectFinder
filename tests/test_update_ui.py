#!/usr/bin/env python3
import time
import sys

# We import Rich directly (which we know is installed because the main app uses it)
try:
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    print("Error: 'rich' library not found. Please run: pip install rich")
    sys.exit(1)

console = Console()

def demo_ui(error_msg):
    """Identical UI logic to what we just added to interface.py"""
    help_text = ""
    title = "Update Failed"
    
    # Logic to detect the type of Git failure
    if "Authentication failed" in error_msg or "password" in error_msg.lower() or "128" in error_msg:
        title = "🔐 GitHub Authentication Issue"
        help_text = (
            "[bold yellow]Reason:[/bold yellow] Your computer lost connection to the GitHub repository.\n\n"
            "[bold cyan]If using the Terminal:[/bold cyan]\n"
            "Run [bold white]git pull[/bold white] manually. It will likely ask you to sign in\n"
            "or enter your Personal Access Token.\n\n"
            "[bold cyan]If using GitHub Desktop:[/bold cyan]\n"
            "1. Sign out and [bold green]Sign back in[/bold green] to GitHub in Settings.\n"
            "2. Try to 'Pull' manually once inside the app."
        )
    elif "could not resolve host" in error_msg.lower():
        title = "🌐 No Internet Connection"
        help_text = "[bold yellow]Reason:[/bold yellow] I can't reach GitHub.com.\n\nCheck your wifi and try again."
    else:
        help_text = f"An unexpected error occurred:\n[dim]{error_msg}[/dim]\n\n[bold yellow]Suggestion:[/bold yellow] Try running 'git pull' manually in your terminal/cmd."

    console.print("\n")
    console.print(Panel(help_text, title=f"[bold red]{title}[/bold red]", border_style="red", expand=False))

def run_demo():
    console.clear()
    console.print(Panel("[bold green]ProjectFinder UI Helper Demo[/bold green]\nSimulating common Git update failures...", border_style="green"))
    time.sleep(1)

    # Simulation 1: Auth Failure
    console.print("\n[bold white]Demo 1: GitHub Authentication Error[/bold white]")
    demo_ui("fatal: Authentication failed for 'https://github.com/u/repo.git'")
    input("\n[dim]Press Enter to see next error...[/dim]")

    # Simulation 2: No Internet
    console.print("\n[bold white]Demo 2: No Internet[/bold white]")
    demo_ui("fatal: unable to access: Could not resolve host: github.com")
    input("\n[dim]Press Enter to see next error...[/dim]")

    # Simulation 3: Generic Error
    console.print("\n[bold white]Demo 3: Generic File Conflict[/bold white]")
    demo_ui("error: Your local changes to 'config.py' would be overwritten by merge")
    
    print("\n✓ Demo Complete.")

if __name__ == "__main__":
    run_demo()
