@echo off
echo =========================================
echo    PYTHON INSTALLATION DEBUG CHECK
echo =========================================
echo.

echo checking 'python'...
python --version 2>nul
if %errorlevel% neq 0 (echo [X] 'python' command NOT found) else (echo [OK] 'python' found)

echo.
echo checking 'py'...
py --version 2>nul
if %errorlevel% neq 0 (echo [X] 'py' command NOT found) else (echo [OK] 'py' found)

echo.
echo checking 'python3'...
python3 --version 2>nul
if %errorlevel% neq 0 (echo [X] 'python3' command NOT found) else (echo [OK] 'python3' found)

echo.
echo =========================================
echo If all of them say [X], you MUST install Python from:
echo https://www.python.org/downloads/
echo =========================================
echo.
pause
