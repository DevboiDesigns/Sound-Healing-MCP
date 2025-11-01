#!/bin/bash
# Quick setup script for Sound Healing MCP Server

echo "🎵 Sound Healing MCP Server Setup"
echo "=================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Found Python $PYTHON_VERSION"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Get absolute path
SERVER_PATH=$(pwd)/server.py
echo ""
echo "✓ Server path: $SERVER_PATH"
echo ""
echo "Next steps:"
echo "1. Copy this path: $SERVER_PATH"
echo "2. Add it to your MCP client configuration"
echo "3. See README.md for client-specific setup instructions"
echo ""
echo "Example configuration:"
echo "{"
echo "  \"mcpServers\": {"
echo "    \"sound-healing\": {"
echo "      \"command\": \"python3\","
echo "      \"args\": [\"$SERVER_PATH\"]"
echo "    }"
echo "  }"
echo "}"
