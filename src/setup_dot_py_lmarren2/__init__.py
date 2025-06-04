"""
Name:
    setup.py

Version:
	0.0.1

Summary:
    Main file that runs all other setup files to initialize a proper python development environment.

Author:
    Luke Marren

Requires:

Date Last Modified:
    June 4, 2025
"""

# =======
# IMPORTS
# =======

from setup_logging import configure_logging
from setup_venv import main as setup_venv

# ==========
# MAIN LOGIC
# ==========

def main():
    configure_logging()
    setup_venv()

if __name__ == "__main__":
    main()
