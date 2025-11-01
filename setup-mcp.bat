@echo off
echo Sound Healing MCP Server Setup
echo ================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo Installing dependencies...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Dependencies installed successfully!
echo.
echo Server path: %CD%\server.py
echo.
echo Next steps:
echo 1. Copy the server path above
echo 2. Add it to your MCP client configuration
echo 3. See README.md for client-specific setup instructions
echo.
pause
