"""
Name:
    setup_logging.py

Version:
	0.0.1

Summary:
    Configures debug logging via the python logging module.

Author:
    Luke Marren

Requires:
    os, logging

Date Last Modified:
    May 30, 2025
"""

# =======
# IMPORTS
# =======

import os
import logging

# =========
# CONSTANTS
# =========

CURRENT_WORKING_DIRECTORY = os.path.normpath(os.getcwd())
LOG_FILE = os.path.join(CURRENT_WORKING_DIRECTORY, "log.txt")
LOG_FORMAT = """%(levelname)s
\t@ %(asctime)s
\ton: %(lineno)d
\tfrom: %(pathname)s
\tmessage: %(message)s
"""

# =========
# UTILITIES
# =========

def configure_logging(log_file: str = LOG_FILE, log_format: str = LOG_FORMAT) -> None:
    """
    Configure basic logging for python app development.

    Args:
        log_file (str): The file path to (over)write log messages to.
        log_format (str): The custom format of the log messages.
    """
    try:
        logging.basicConfig(filename=log_file,
                    filemode="w",
                    format=log_format,
                    level=logging.DEBUG,
                    force=True,
                    encoding="utf-8")
        logging.info("Successfully configured logging.")
    except Exception as e:
        logging.error(f"Failed to configure logging due to {e}.\nPlease check {LOG_FILE} for more details.")

# ==========
# MAIN LOGIC
# ==========

def main() -> None:
    """
    Main function of setup_logging.py.
    """
    configure_logging()

if __name__ == "__main__":
    main()
