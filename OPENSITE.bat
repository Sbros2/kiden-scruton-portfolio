@echo off
cd /d "%~dp0"
start "Proposed portfolio" cmd /k "npm run dev -- --port 4322"
timeout /t 5 /nobreak > NUL
start http://localhost:4322
