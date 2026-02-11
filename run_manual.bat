@echo off
REM Manual run with popup notification
cd /d "%~dp0"
echo Running scraper manually...
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Running scraper manually...
python run_scraper.py --notify popup
echo.
pause
