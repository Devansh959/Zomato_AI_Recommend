@echo off
set PATH=%PATH%;C:\Program Files\Git\cmd
echo Fixing large file issues and setting up Git LFS...

REM Initialize Git LFS
git lfs install

REM Ensure we track the database with LFS
git add .gitattributes

REM Nuke and reset the git history to safely remove the large files from cache
rmdir /S /Q .git
git init

REM Setup LFS again just in case for the new git init
git lfs install
git add .gitattributes
git add data/zomato.sqlite
git commit -m "chore: track sqlite database with git lfs"

REM Add the rest of the project
git add .
git commit -m "feat: complete Zomato UI overhaul and Docker setup"

REM Push to GitHub
git branch -M main
git remote add origin https://github.com/Devansh959/Zomato_AI_Recommend.git
git push -u origin main --force
pause
