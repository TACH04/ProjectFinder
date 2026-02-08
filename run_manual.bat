@echo off
REM Manual run with popup notification
cd /d "%~dp0"
echo Running scraper manually...
.venv\Scripts\python.exe run_scraper.py --notify popup
echo.
pause
