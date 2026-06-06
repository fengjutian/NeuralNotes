#!/usr/bin/env python
"""
NeuralNotes Startup Script
Starts both frontend and backend servers with dependency checks.
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
BACKEND_DIR = PROJECT_ROOT / "backend"
FRONTEND_DIR = PROJECT_ROOT / "frontend"


def check_node_modules():
    """Check if frontend node_modules exists."""
    node_modules = FRONTEND_DIR / "node_modules"
    if not node_modules.exists():
        print("❌ Frontend dependencies not found.")
        print(f"   Please run: cd {FRONTEND_DIR} && npm install")
        return False
    print("✅ Frontend dependencies OK")
    return True


def check_python_venv():
    """Check if backend venv exists."""
    venv_path = BACKEND_DIR / "venv"
    if not venv_path.exists():
        print("❌ Python virtual environment not found.")
        print(f"   Please run: cd {BACKEND_DIR} && python -m venv venv")
        return False
    print("✅ Python virtual environment OK")
    return True


def check_env_file():
    """Check if backend .env file exists."""
    env_path = BACKEND_DIR / ".env"
    env_example = BACKEND_DIR / "env_example.txt"
    if not env_path.exists():
        if env_example.exists():
            print("⚠️  Backend .env file not found. Copying from env_example.txt...")
            shutil.copy(env_example, env_path)
            print(f"   Please edit {env_path} and fill in your configuration")
        else:
            print("⚠️  Backend .env file not found (env_example.txt also missing)")
    else:
        print("✅ Backend .env file OK")
    return True


def start_backend():
    """Start the backend server."""
    print("\n🚀 Starting backend server...")
    
    # Determine Python executable in venv
    if os.name == "nt":  # Windows
        python_exe = BACKEND_DIR / "venv" / "Scripts" / "python.exe"
    else:  # Unix
        python_exe = BACKEND_DIR / "venv" / "bin" / "python"
    
    if not python_exe.exists():
        print(f"❌ Python executable not found at {python_exe}")
        return None
    
    # Start uvicorn
    backend_proc = subprocess.Popen(
        [str(python_exe), "-m", "uvicorn", "src.main:app",
         "--host", "127.0.0.1", "--port", "8000", "--reload"],
        cwd=str(BACKEND_DIR),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    print("✅ Backend server started on http://127.0.0.1:8000")
    return backend_proc


def start_frontend():
    """Start the frontend dev server."""
    print("\n🚀 Starting frontend server...")
    
    # Check if npm is available
    npm_exe = shutil.which("npm")
    if not npm_exe:
        print("❌ npm not found in PATH")
        return None
    
    # Start Vite dev server
    frontend_proc = subprocess.Popen(
        [npm_exe, "run", "dev"],
        cwd=str(FRONTEND_DIR),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    print("✅ Frontend server starting on http://localhost:5174")
    return frontend_proc


def main():
    print("=" * 50)
    print("NeuralNotes Startup Check")
    print("=" * 50)
    
    # Run dependency checks
    checks_passed = True
    checks_passed &= check_node_modules()
    checks_passed &= check_python_venv()
    check_env_file()  # This creates .env if missing, so always returns True
    
    if not checks_passed:
        print("\n❌ Dependency checks failed. Please fix the issues above.")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("Starting servers...")
    print("=" * 50)
    
    # Start backend
    backend_proc = start_backend()
    
    # Start frontend
    frontend_proc = start_frontend()
    
    print("\n✅ All servers started successfully!")
    print("   Frontend: http://localhost:5174")
    print("   Backend:  http://127.0.0.1:8000")
    print("\nPress Ctrl+C to stop all servers")
    
    try:
        # Wait for both processes
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down servers...")
        for proc in [backend_proc, frontend_proc]:
            if proc:
                proc.terminate()
        print("✅ Servers stopped")


if __name__ == "__main__":
    main()