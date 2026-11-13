@echo off
cd /d "%~dp0"
echo Launching Pearls of the Past...
python -m streamlit run app.py
pause
