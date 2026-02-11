@echo off
REM Double-click to run the scraper (run_scraper.py)

cd /d "%~dp0"
echo Running scraper...
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Running scraper...
python run_scraper.py %*
echo.
echo Done!
pause
