#!/usr/bin/env python3
"""
Test script for verification of notification logic
"""
import os
import json
import shutil
from datetime import datetime

from scraper.scraper import Project
from scraper.notifications import check_for_new_projects
from config import SEEN_PROJECTS_FILE, DATA_DIR

import tempfile

# Test file path (use system temp dir)
TEST_SEEN_FILE = os.path.join(tempfile.gettempdir(), "test_seen_projects.json")

def setup():
    """Ensure test environment is clean"""
    # Just ensure the test file doesn't exist
    if os.path.exists(TEST_SEEN_FILE):
        os.remove(TEST_SEEN_FILE)
        
    # Monkeypatch the config in notifications module
    # We need to modify the imported variable in scraper.notifications
    import scraper.notifications
    scraper.notifications.SEEN_PROJECTS_FILE = TEST_SEEN_FILE

def teardown():
    """Cleanup test file"""
    if os.path.exists(TEST_SEEN_FILE):
        os.remove(TEST_SEEN_FILE)
    print("\n🔄 Cleaned up test data.")

def create_dummy_project(pid, title):
    return Project(
        id=str(pid),
        title=title,
        portal="test_portal",
        url="http://example.com",
        release_date=datetime.now()
    )

def run_tests():
    print("🧪 Starting Notification Logic Tests...")
    
    try:
        # TEST 1: First Run (Fresh State)
        print("\n[TEST 1] First Run (Fresh State)")
        projects_run1 = [
            create_dummy_project(1, "Project A"),
            create_dummy_project(2, "Project B"),
        ]
        
        new1, _ = check_for_new_projects(projects_run1)
        
        assert len(new1) == 2, f"Expected 2 new projects, got {len(new1)}"
        assert new1[0].id == "1"
        print("  ✓ Correctly identified all projects as new on first run.")
        
        # TEST 2: Second Run (No Changes)
        print("\n[TEST 2] Second Run (No Changes)")
        projects_run2 = [
            create_dummy_project(1, "Project A"),
            create_dummy_project(2, "Project B"),
        ]
        
        new2, _ = check_for_new_projects(projects_run2)
        
        assert len(new2) == 0, f"Expected 0 new projects, got {len(new2)}"
        print("  ✓ Correctly identified 0 new projects on second run.")
        
        # TEST 3: New Project Added
        print("\n[TEST 3] New Project Added")
        projects_run3 = [
            create_dummy_project(1, "Project A"),
            create_dummy_project(2, "Project B"),
            create_dummy_project(3, "Project C (NEW)"),
        ]
        
        new3, _ = check_for_new_projects(projects_run3)
        
        assert len(new3) == 1, f"Expected 1 new project, got {len(new3)}"
        assert new3[0].id == "3"
        print("  ✓ Correctly identified exactly 1 new project.")
        
        print("\n✅ ALL TESTS PASSED!")
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False

def main():
    setup()
    try:
        run_tests()
    finally:
        teardown()

if __name__ == "__main__":
    main()
