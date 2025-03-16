import os
import logging

def setup_logging():
    """
    Configures the logging system based on environment variables.
    """
    # Default settings
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()  # Default to INFO if not set
    log_file = os.getenv("LOG_FILE", None)  # Default to console output

    # Create the logging configuration
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),  # Set log level
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file) if log_file else logging.StreamHandler()
        ]
    )