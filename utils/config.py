import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    def __init__(self):
        history_file = os.getenv("HISTORY_FILE")
        self.history_file = history_file if history_file and history_file.strip() else "history.csv"