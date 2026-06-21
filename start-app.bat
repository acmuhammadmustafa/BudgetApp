@echo off
REM Budget App Launcher - Double-click to run!

cd /d "%~dp0"

echo.
echo =================================================
echo   Budget App Launcher
echo =================================================
echo.
echo Starting services...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found in PATH
    echo Please install Python and add it to your PATH
    pause
    exit /b 1
)

REM Check if Node.js is installed
npm --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js/npm not found in PATH
    echo Please install Node.js
    pause
    exit /b 1
)

echo Starting Backend API Server (port 8000)...
start cmd /k "cd backend && venv\Scripts\activate && python main.py"

timeout /t 2 /nobreak

echo Starting Frontend Dev Server (port 5173)...
start cmd /k "cd frontend && npm run dev"

timeout /t 3 /nobreak

echo.
echo =================================================
echo   Budget App is now running!
echo =================================================
echo.
echo Opening app in browser...
start http://localhost:5173

echo.
echo API Server: http://localhost:8000
echo App URL:    http://localhost:5173
echo.
echo To stop the app, close both terminal windows.
echo.
pause
