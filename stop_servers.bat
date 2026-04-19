@echo off
echo Stopping FastAPI backend...
taskkill /IM uvicorn.exe /F 2>NUL

echo Stopping Next.js frontend...
taskkill /IM node.exe /F 2>NUL

echo All background servers have been stopped!
pause
