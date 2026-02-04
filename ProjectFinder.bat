@echo off
REM Double-click this file to run ProjectFinder manually

cd /d "%~dp0"
echo Running ProjectFinder...
.venv\Scripts\python.exe main.py
echo.
echo Done!
pause
