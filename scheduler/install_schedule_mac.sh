#!/bin/bash
# macOS LaunchAgent Installer for ProjectFinder
# Runs the scraper daily at 7:00 AM

PLIST_NAME="com.projectfinder.daily"
PLIST_PATH="$HOME/Library/LaunchAgents/$PLIST_NAME.plist"
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "📦 Installing ProjectFinder daily scheduler..."

# Create LaunchAgents directory if it doesn't exist
mkdir -p "$HOME/Library/LaunchAgents"

# Create the plist file
cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$PLIST_NAME</string>
    
        <string>$PROJECT_DIR/.venv/bin/python3</string>
        <string>$PROJECT_DIR/run_scraper.py</string>
    </array>
    
    <key>WorkingDirectory</key>
    <string>$PROJECT_DIR</string>
    
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    
    <key>StandardOutPath</key>
    <string>$PROJECT_DIR/logs/scraper.log</string>
    
    <key>StandardErrorPath</key>
    <string>$PROJECT_DIR/logs/scraper_error.log</string>
    
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin</string>
    </dict>
</dict>
</plist>
EOF

# Create logs directory
mkdir -p "$PROJECT_DIR/logs"

# Load the agent
launchctl unload "$PLIST_PATH" 2>/dev/null
launchctl load "$PLIST_PATH"

echo "✅ Scheduler installed!"
echo "   Runs daily at 7:00 AM"
echo "   Logs: $PROJECT_DIR/logs/"
echo ""
echo "Commands:"
echo "   Uninstall: launchctl unload $PLIST_PATH && rm $PLIST_PATH"
echo "   Run now:   launchctl start $PLIST_NAME"
echo "   Check:     launchctl list | grep projectfinder"
