import subprocess
import os
import time


def start_servers():
    # Start Python WebSocket server
    python_server_cmd = ["python3", "python/server.py"]
    python_server_process = subprocess.Popen(python_server_cmd)

    # Wait for the WebSocket server to start (optional)
    time.sleep(2)  # Adjust as needed

    # Change directory to React app directory
    os.chdir(
        "/Users/jamesfitzsimons/Developer/websockets test/websockets"
    )  # Replace with your React app directory

    # Start React development server
    react_server_cmd = ["npm", "run", "dev"]
    react_server_process = subprocess.Popen(react_server_cmd)

    # Optionally, wait for processes to finish (if needed)
    python_server_process.wait()
    react_server_process.wait()


if __name__ == "__main__":
    start_servers()
