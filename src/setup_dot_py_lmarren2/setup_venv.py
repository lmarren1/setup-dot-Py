"""
Name:
    setup_venv.py

Version:
	0.0.1

Summary:
    Creates a python virtual environment if none already exists.

Author:
    Luke Marren

Requires:
    os, subprocess, sys, logging

Date Last Modified:
    May 30, 2025
"""

# =======
# IMPORTS
# =======

import os
import subprocess
import sys
import logging
from setup_logging import CURRENT_WORKING_DIRECTORY

# =========
# CONSTANTS
# =========

VENV_PATH = os.path.join(CURRENT_WORKING_DIRECTORY, "venv")

# =========
# UTILITIES
# =========

def venv_exists(venv_path: str = VENV_PATH):
    if os.path.exists(VENV_PATH):
        logging.warning(f"Virtual environment already exists at {venv_path}.\nAborting virtual environment creation.")
        return True
    else:
        logging.info("No virtual environment detected.")
        return False

def create_venv(venv_path: str = VENV_PATH):
    try:
        logging.info("Starting virtual environment creation.")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        logging.info(f"Successfully created virtual environment at: {venv_path}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while creating virtual environment: {e}.")
    
# ==========
# MAIN LOGIC
# ==========

def main():
    if venv_exists():
        create_venv()

if __name__ == "__main__":
    main()
