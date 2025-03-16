import pandas as pd
import os
import logging

class HistoryManager:
    def __init__(self):
        config = Config()
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
        self.filepath = "history.csv"
        self.logger = logging.getLogger(__name__)
    
    def add_to_history(self, operation, operand1, operand2, result):
        """
        Add a new record to the history.
        """
        new_entry = {
            "Operation": operation,
            "Operand1": operand1,
            "Operand2": operand2,
            "Result": result,
        }
        self.history = self.history.append(new_entry, ignore_index=True)
        self.logger.info("Added new record to history.")
    
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
            print("No history file to load.")
    
    def clear_history(self):
        """
        Clear the history.
        """
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
        self.logger.info("Cleared history.")