import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class to manage environment variables.
    """
    @property
    def history_file(self):
        return os.getenv("HISTORY_FILE", "history.csv")

    @property
    def log_level(self):
        return os.getenv("LOG_LEVEL", "INFO")

    @property
    def log_file(self):
        return os.getenv("LOG_FILE", None)