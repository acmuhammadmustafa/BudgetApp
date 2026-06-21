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
        # Start backend
        print("🔧 Starting backend API server (port 8000)...")
        backend_venv = backend_dir / "venv" / "Scripts" / "python.exe"

        if not backend_venv.exists():
            print("❌ Error: Backend virtual environment not found")
            print("   Please run: cd backend && python -m venv venv")
            sys.exit(1)

        backend_process = subprocess.Popen(
            [str(backend_venv), "main.py"],
            cwd=str(backend_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
        )
        print("✅ Backend started!")
        time.sleep(2)

        # Start frontend
        print("⚛️  Starting frontend dev server (port 5173)...")
        frontend_process = subprocess.Popen(
            ["npm", "run", "dev"],
            cwd=str(frontend_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
        )
        print("✅ Frontend started!")
        time.sleep(3)

        # Open browser
        print()
        print("🌐 Opening app in browser...")
        webbrowser.open("http://localhost:5173")

        print()
        print("=" * 50)
        print("✨ Budget App is running!")
        print("=" * 50)
        print()
        print("📱 App URL: http://localhost:5173")
        print("🔌 API URL: http://localhost:8000")
        print()
        print("📝 To stop the app, close both terminal windows")
        print("   or press Ctrl+C in the windows")
        print()
        print("=" * 50)

        # Keep the launcher running
        while True:
            time.sleep(1)
            # Check if processes are still running
            if backend_process.poll() is not None:
                print("❌ Backend process stopped!")
                break
            if frontend_process.poll() is not None:
                print("❌ Frontend process stopped!")
                break

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("   Make sure Node.js and Python are installed and in your PATH")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
        time.sleep(1)
        backend_process.kill()
        frontend_process.kill()
        print("✅ Budget App stopped")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
