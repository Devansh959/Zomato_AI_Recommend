import subprocess
import os

print("Terminating old servers...")
os.system('taskkill /IM uvicorn.exe /F 2>NUL')
os.system('taskkill /IM streamlit.exe /F 2>NUL')

print("Starting FastAPI and Streamlit in the background...")
subprocess.Popen([r'.\venv\Scripts\uvicorn.exe', 'src.main:app', '--port', '8000'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

subprocess.Popen([r'.\venv\Scripts\streamlit.exe', 'run', r'src\app.py', '--server.headless', 'true'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

print("Servers are successfully running! Please open your browser.")
