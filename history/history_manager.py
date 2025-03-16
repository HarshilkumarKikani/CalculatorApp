import pandas as pd
import os
import logging
from utils.config import Config

class HistoryManager:
    def __init__(self):
        config = Config()  # Declared and use config
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
        self.filepath = config.history_file
        self.logger = logging.getLogger(__name__)
    
    def add_to_history(self, operation, operand1, operand2, result):
        """
        Add a new record to the history.
        """
        new_entry = pd.DataFrame([{
            "Operation": operation,
            "Operand1": operand1,
            "Operand2": operand2,
            "Result": result,
        }])

        # Explicitly check if self.history is empty
        if self.history.empty:
            self.history = new_entry  # Set directly if empty
        else:
            self.history = pd.concat([self.history, new_entry], ignore_index=True)
    
    def display_history(self):
        """
        Return a string representation of the history.
        """
        if self.history.empty:
            return "No history available."
        return self.history.to_string(index=False)
    
    def save_history(self):
        """
        Save the history to a CSV file.
        """
        self.history.to_csv(self.filepath, index=False)
        self.logger.info(f"History saved to {self.filepath}")
    
    def load_history(self):
        """
        Load the history from a CSV file.
        """
        if os.path.exists(self.filepath):
            self.history = pd.read_csv(self.filepath)
            self.logger.info(f"History loaded from {self.filepath}")
        else:
            self.logger.warning(f"No history file found at {self.filepath}")
            raise FileNotFoundError(f"No file found at {self.filepath}")
    
    def clear_history(self):
        """
        Clear the history.
        """
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
        self.logger.info("Cleared history.")