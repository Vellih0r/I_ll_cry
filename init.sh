#!/bin/bash
set -e  # Stop scrept if error caused

echo "Step 1: Checking Python and pip..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install it and try again."
    exit 1
fi

if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install it and try again."
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "Creating .venv..."
    python3 -m venv .venv
fi

echo "Activating .venv..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

echo "Step 2: Installing required Python packages..."
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found. Please provide it and try again."
    exit 1
fi
pip install -r requirements.txt

echo "Step 3: Building the project..."
pyinstaller --add-binary /usr/lib/x86_64-linux-gnu/libpython3.11.so.1.0:. --onefile ./helpme.py
mv ./dist/helpme ./

echo "Step 4: Cleaning up..."
deactivate
rm -rf dist/ helpme.spec build/

# check if ~/bin not exists
if [ ! -d "$HOME/bin" ]; then
    echo "Creating ~/bin directory..."
    mkdir -p "$HOME/bin"
fi

# adding ~/bin in PATH if it not there yet
if ! echo "$PATH" | grep -q "$HOME/bin"; then
    echo "Adding ~/bin to PATH..."
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
    source "$HOME/.bashrc"
fi

mv helpme ~/bin

echo "Done!"

