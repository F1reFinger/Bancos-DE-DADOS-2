#!/bin/bash

# Define target folder
VENV_DIR="DIRETORIO DO VENV"

# Step 1: Create folder if not exists
mkdir -p "$VENV_DIR"

# Step 2: Create virtual environment
python3 -m venv "$VENV_DIR"

# Step 3: Activate venv and install dependencies
source "$VENV_DIR/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install requests pandas beautifulsoup4 lxml jupyter

# Step 4: Confirm installation
echo "✅ Virtual environment created at $VENV_DIR"
echo "✅ Dependencies installed: requests, pandas, beautifulsoup4, lxml, jupyter"
echo
echo "👉 To activate it later, run:"
echo "   source $VENV_DIR/bin/activate"
