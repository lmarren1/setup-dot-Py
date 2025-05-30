#!/bin/bash

# Path to the virtual environment
VENV_PATH="/home/pi/medusa/venv"
REQ_FILE="/home/pi/medusa/requirements.txt"

# Activate the virtual environment
echo "================================="
echo "Activating virtual environment..."
echo "================================="

source "$VENV_PATH/bin/activate"

# Upgrade pip
echo "================================="
echo "Upgrading pip..."
echo "================================="

pip install --upgrade pip

# Upgrade setuptools and wheel (best practice)
echo "================================="
echo "Upgrading setuptools and wheel..."
echo "================================="

pip install --upgrade setuptools wheel

# Update requirements.txt
echo "================================="
echo "Updating requirements.txt..."
echo "================================="

pip freeze > requirements.txt

# Upgrade requirements.txt
echo "================================="
echo "Upgrading packages from requirements.txt..."
echo "================================="

pip install --upgrade -r "$REQ_FILE"

# Update requirements.txt so that any upgrades are reflected there
echo "================================="
echo "Updating requirements.txt Again..."
echo "================================="

pip freeze > requirements.txt

# Deactivate the virtual environment
deactivate

echo "================================="
echo "Update complete."
echo "================================="
