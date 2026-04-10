@echo off
setlocal enabledelayedexpansion
title Agriculture Predictor Launcher
echo ==========================================
echo    AGRICULTURE CROP PREDICTOR LAUNCHER
echo ==========================================
echo.

:: --- FIND THE CORRECT PYTHON COMMAND ---
set PY_CMD=none
for %%i in (python py python3) do (
    %%i --version >nul 2>&1
    if !errorlevel! equ 0 (
        set PY_CMD=%%i
        goto :found
    )
)

:found
if "%PY_CMD%"=="none" (
    echo [ERROR] Python not found on your system!
    echo Please install Python from https://www.python.org/downloads/
    echo During installation, check "Add Python to PATH".
    pause
    exit /b
)

echo [OK] Using command: %PY_CMD%
echo.

echo [1/4] Checking Libraries...
%PY_CMD% -m pip install flask pandas scikit-learn numpy

echo.
echo [2/4] Preparing the AI Brain...
%PY_CMD% train_and_save.py

echo.
echo [3/4] Starting the Website Server...
echo Your website will open in 3 seconds...
timeout /t 3 >nul

echo.
echo [4/4] Opening Website Link...
start "" "http://127.0.0.1:5000"

echo.
echo Server is running! DO NOT CLOSE THIS WINDOW.
%PY_CMD% app.py
pause
