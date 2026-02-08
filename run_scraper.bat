@echo off
REM Double-click to run the scraper (run_scraper.py)

cd /d "%~dp0"
echo Running scraper...
.venv\Scripts\python.exe run_scraper.py
echo.
echo Done!
pause
