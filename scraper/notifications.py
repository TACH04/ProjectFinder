"""
New project detection and notification system
"""

import json
import os
from datetime import datetime, date
from typing import List, Set, Tuple

from config import DATA_DIR, SEEN_PROJECTS_FILE
from scraper.scraper import Project


def ensure_data_dir():
    """Ensure data directory exists"""
    os.makedirs(DATA_DIR, exist_ok=True)


def load_seen_projects() -> dict:
    """Load previously seen projects from JSON file"""
    ensure_data_dir()
    
    if os.path.exists(SEEN_PROJECTS_FILE):
        try:
            with open(SEEN_PROJECTS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"projects": {}, "last_check": None}
    
    return {"projects": {}, "last_check": None}


def save_seen_projects(data: dict):
    """Save seen projects to JSON file"""
    ensure_data_dir()
    
    data["last_check"] = datetime.now().isoformat()
    with open(SEEN_PROJECTS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def get_project_key(project: Project) -> str:
    """Generate unique key for a project"""
    return f"{project.portal}:{project.id}"


def check_for_new_projects(projects: List[Project]) -> Tuple[List[Project], List[Project]]:
    """
    Compare current projects against previously seen ones
    
    Returns:
        Tuple of (new_projects, todays_projects)
    """
    seen_data = load_seen_projects()
    seen_keys: Set[str] = set(seen_data["projects"].keys())
    
    new_projects = []
    todays_projects = []
    
    for project in projects:
        key = get_project_key(project)
        
        # Check if this is a new project we haven't seen before
        if key not in seen_keys:
            new_projects.append(project)
            # Add to seen projects
            seen_data["projects"][key] = {
                "first_seen": datetime.now().isoformat(),
                "data": project.to_dict(),
            }
        
        # Check if released today
        if project.is_from_today():
            todays_projects.append(project)
    
    # Save updated seen projects
    save_seen_projects(seen_data)
    
    return new_projects, todays_projects


def notify_new_projects(new_projects: List[Project], todays_projects: List[Project]):
    """Display notification for new/today's projects"""
    
    print("\n" + "=" * 60)
    print("📋 PROJECT FINDER RESULTS")
    print("=" * 60)
    print(f"Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Today's projects
    if todays_projects:
        print(f"\n🆕 PROJECTS RELEASED TODAY ({len(todays_projects)}):")
        print("-" * 40)
        for p in todays_projects:
            print(f"  • [{p.portal}] {p.title}")
            print(f"    Release Date: {p.release_date}")
            if p.url:
                print(f"    URL: {p.url}")
            print()
    else:
        print("\n✓ No new projects released today.")
    
    # New projects (first time seeing them)
    if new_projects:
        print(f"\n📌 NEW PROJECTS DETECTED ({len(new_projects)}):")
        print("-" * 40)
        for p in new_projects:
            print(f"  • [{p.portal}] {p.title}")
            print(f"    ID: {p.id} | Status: {p.status}")
            if p.release_date != "Unknown":
                print(f"    Release Date: {p.release_date}")
            if p.url:
                print(f"    URL: {p.url}")
            print()
    else:
        print("\n✓ No previously unseen projects found.")
    
    print("=" * 60)
    
    # Return summary
    return {
        "new_count": len(new_projects),
        "today_count": len(todays_projects),
        "new_projects": [p.to_dict() for p in new_projects],
        "todays_projects": [p.to_dict() for p in todays_projects],
    }
