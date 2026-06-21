#!/usr/bin/env python3
"""
Budget App Launcher
Starts both the backend (FastAPI) and frontend (Vite) servers
and automatically opens the app in your default browser.
"""

import subprocess
import time
import os
import sys
import webbrowser
from pathlib import Path
import shutil


def main():
    # Get the project root directory
    project_root = Path(__file__).parent
    backend_dir = project_root / "backend"
    frontend_dir = project_root / "frontend"

    print("🚀 Budget App Launcher")
    print("=" * 50)
    print()

    # Check if directories exist
    if not backend_dir.exists() or not frontend_dir.exists():
        print("❌ Error: Could not find backend or frontend directories")
        sys.exit(1)

    print("📦 Starting services...")
    print()

    try:
        # Check Python venv
        print("🔧 Checking Python virtual environment...")
        backend_venv = backend_dir / "venv" / "Scripts" / "python.exe"

        if not backend_venv.exists():
            print("❌ Error: Backend virtual environment not found")
            print(
                "   Please run: cd backend && python -m venv venv && pip install -r requirements.txt")
            sys.exit(1)
        print("✅ Python environment found")

        # Check npm
        print("🔧 Checking Node.js/npm...")
        npm_path = shutil.which("npm")
        if not npm_path:
            print("❌ Error: npm not found in PATH")
            print("   Please install Node.js from https://nodejs.org/")
            sys.exit(1)
        print("✅ npm found")

        # Start backend in new window
        print()
        print("🔧 Starting backend API server (port 8000)...")
        backend_cmd = f'cd /d "{backend_dir}" && venv\\Scripts\\activate.bat && python main.py'
        backend_process = subprocess.Popen(
            backend_cmd,
            shell=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
        )
        print("✅ Backend started in new window!")
        time.sleep(3)

        # Start frontend in new window
        print()
        print("⚛️  Starting frontend dev server (port 5173)...")
        frontend_cmd = f'cd /d "{frontend_dir}" && npm run dev'
        frontend_process = subprocess.Popen(
            frontend_cmd,
            shell=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
        )
        print("✅ Frontend started in new window!")
        time.sleep(4)

        # Open browser
        print()
        print("🌐 Opening app in browser...")
        webbrowser.open("http://localhost:5173")
        time.sleep(1)

        print()
        print("=" * 50)
        print("✨ Budget App is running!")
        print("=" * 50)
        print()
        print("📱 App URL:    http://localhost:5173")
        print("🔌 API URL:    http://localhost:8000")
        print()
        print("💡 The app has opened in your default browser.")
        print("   If it didn't open, manually visit: http://localhost:5173")
        print()
        print("📝 Both servers are running in separate windows.")
        print("   Close those windows to stop the app.")
        print()
        print("=" * 50)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
