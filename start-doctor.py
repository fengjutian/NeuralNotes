#!/usr/bin/env python
"""
NeuralNotes Startup Script
Starts both frontend and backend servers with dependency checks.
"""
import os
import sys
import subprocess
import shutil
import socket
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
BACKEND_DIR = PROJECT_ROOT / "backend"
FRONTEND_DIR = PROJECT_ROOT / "frontend"
FRONTEND_PORT = 5174
BACKEND_PORT = 8020


def check_port(port):
    """Check if a port is in use."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        return result == 0  # True if port is in use
    except Exception:
        return False


def kill_port(port):
    """Kill all processes using the specified port."""
    try:
        # Windows: use PowerShell to find and kill all processes on port
        ps_script = f'''
        $connections = Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue
        if ($connections) {{
            $pids = $connections | Select-Object -ExpandProperty OwningProcess -Unique
            foreach ($pid in $pids) {{
                Write-Host "Killing PID: $pid"
                Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue
            }}
        }}
        '''
        result = subprocess.run(
            ['powershell', '-Command', ps_script],
            capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
        )
        if 'Killing' in result.stdout:
            print(f"   Killed processes on port {port}")
            import time
            time.sleep(1)  # Give OS time to release port
            return True
    except Exception as e:
        print(f"   Failed to kill process on port {port}: {e}")
    return False


def check_ports(auto_kill=False):
    """Check if required ports are available."""
    frontend_in_use = check_port(FRONTEND_PORT)
    backend_in_use = check_port(BACKEND_PORT)
    
    if not frontend_in_use and not backend_in_use:
        return True
    
    if frontend_in_use:
        print(f"⚠️  Port {FRONTEND_PORT} (frontend) is already in use")
        if auto_kill:
            kill_port(FRONTEND_PORT)
            if check_port(FRONTEND_PORT):
                print(f"❌ Failed to free port {FRONTEND_PORT}")
                return False
    
    if backend_in_use:
        print(f"⚠️  Port {BACKEND_PORT} (backend) is already in use")
        if auto_kill:
            kill_port(BACKEND_PORT)
            if check_port(BACKEND_PORT):
                print(f"❌ Failed to free port {BACKEND_PORT}")
                return False
    
    # Recheck after killing
    frontend_ok = not check_port(FRONTEND_PORT)
    backend_ok = not check_port(BACKEND_PORT)
    
    if not frontend_ok:
        print(f"❌ Port {FRONTEND_PORT} (frontend) is still in use")
    if not backend_ok:
        print(f"❌ Port {BACKEND_PORT} (backend) is still in use")
    
    return frontend_ok and backend_ok


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
        # Output to files - use append mode and don't close handles
        stdout_file = open(PROJECT_ROOT / "backend_out.log", "a")
        stderr_file = open(PROJECT_ROOT / "backend_err.log", "a")
        backend_proc = subprocess.Popen(
            [str(python_exe), "-m", "uvicorn", "src.main:app",
             "--host", "127.0.0.1", "--port", str(BACKEND_PORT), "--reload"],
            cwd=str(BACKEND_DIR),
            stdout=stdout_file,
            stderr=stderr_file,
            bufsize=1  # Line buffered
        )
        print(f"✅ Backend server started on http://127.0.0.1:{BACKEND_PORT}")
        return backend_proc
    else:  # Unix
        python_exe = BACKEND_DIR / "venv" / "bin" / "python"
        backend_proc = subprocess.Popen(
            [str(python_exe), "-m", "uvicorn", "src.main:app",
             "--host", "127.0.0.1", "--port", str(BACKEND_PORT), "--reload"],
            cwd=str(BACKEND_DIR)
        )
        print(f"✅ Backend server started on http://127.0.0.1:{BACKEND_PORT}")
        return backend_proc


def start_frontend():
    """Start the frontend dev server."""
    print("\n🚀 Starting frontend server...")
    
    # Check if npm is available
    npm_exe = shutil.which("npm")
    if not npm_exe:
        print("❌ npm not found in PATH")
        return None
    
    if os.name == "nt":  # Windows
        stdout_file = open(PROJECT_ROOT / "frontend_out.log", "a")
        stderr_file = open(PROJECT_ROOT / "frontend_err.log", "a")
        frontend_proc = subprocess.Popen(
            [npm_exe, "run", "dev"],
            cwd=str(FRONTEND_DIR),
            stdout=stdout_file,
            stderr=stderr_file,
            bufsize=1  # Line buffered
        )
        print(f"✅ Frontend server starting on http://localhost:{FRONTEND_PORT}")
        return frontend_proc
    else:  # Unix
        frontend_proc = subprocess.Popen(
            [npm_exe, "run", "dev"],
            cwd=str(FRONTEND_DIR)
        )
        print(f"✅ Frontend server starting on http://localhost:{FRONTEND_PORT}")
        return frontend_proc


def main():
    print("=" * 50)
    print("NeuralNotes Startup Check")
    print("=" * 50)
    
    # Check ports first
    print("\n🔍 Checking ports...")
    if not check_ports(auto_kill=True):
        print("\n❌ Port check failed.")
        sys.exit(1)
    print(f"✅ Ports {FRONTEND_PORT} and {BACKEND_PORT} are available")
    
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
    print(f"   Frontend: http://localhost:{FRONTEND_PORT}")
    print(f"   Backend:  http://127.0.0.1:{BACKEND_PORT}")
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