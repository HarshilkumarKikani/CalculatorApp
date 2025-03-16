import os
import sys
import logging
from utils.logging_config import setup_logging
from history.history_manager import HistoryManager
from plugins import basic_operations, statistics_operations

def main():
    # Set up logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Initialize history manager
    history_manager = HistoryManager()

    print("Welcome to the Advanced Calculator!")
    logger.info("Application started")
    while True:
        try:
            command = input(">> ").strip().lower()
            if command == "exit":
                print("Goodbye!")
                logger.info("Application exited")
                break
            elif command == "menu":
                print("Available commands: add, subtract, multiply, divide, mean, median, mode, history, clear, save, load, exit")
            elif command.startswith("add") or command.startswith("subtract") or \
                 command.startswith("multiply") or command.startswith("divide"):
                # Delegate to plugin for basic operations
                result = basic_operations.execute(command, history_manager)
                print(f"Result: {result}")
            elif command.startswith("mean") or command.startswith("median") or command.startswith("mode"):
                result = statistics_operations.execute(command, history_manager)
                print(f"Result: {result}")
            elif command == "history":
                print(history_manager.display_history())
            elif command == "clear":
                history_manager.clear_history()
                print("History cleared!")
            elif command.startswith("save"):
                history_manager.save_history()
                print("History saved!")
            elif command.startswith("load"):
                history_manager.load_history()
                print("History loaded!")
            else:
                print("Unknown command. Type 'menu' for options.")
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
