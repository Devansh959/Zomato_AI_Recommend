@echo off
echo Starting FastAPI Backend...
start cmd /k ".\venv\Scripts\uvicorn.exe src.main:app --port 8000"

echo Starting Streamlit Frontend...
start cmd /k ".\venv\Scripts\streamlit.exe run src\app.py"

echo Both services have been started in separate windows!
