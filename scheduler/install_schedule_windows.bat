@echo off
REM Windows Task Scheduler Installer for ProjectFinder
REM Runs the scraper daily at 7:00 AM

set TASK_NAME=ProjectFinder Daily Check
set PROJECT_DIR=%~dp0

echo Installing ProjectFinder daily scheduler...

REM Create logs directory
if not exist "%PROJECT_DIR%logs" mkdir "%PROJECT_DIR%logs"

REM Delete existing task if present
schtasks /delete /tn "%TASK_NAME%" /f 2>nul

REM Create the scheduled task
schtasks /create ^
    /tn "%TASK_NAME%" ^
    /tr "\"%PROJECT_DIR%.venv\Scripts\python.exe\" \"%PROJECT_DIR%main.py\" --headless" ^
    /sc daily ^
    /st 07:00 ^
    /rl highest

if %ERRORLEVEL% == 0 (
    echo.
    echo ✅ Scheduler installed!
    echo    Runs daily at 7:00 AM
    echo    Logs: %PROJECT_DIR%logs\
    echo.
    echo Commands:
    echo    Uninstall: schtasks /delete /tn "%TASK_NAME%" /f
    echo    Run now:   schtasks /run /tn "%TASK_NAME%"
    echo    Check:     schtasks /query /tn "%TASK_NAME%"
) else (
    echo ❌ Failed to create scheduled task. Try running as Administrator.
)
pause
