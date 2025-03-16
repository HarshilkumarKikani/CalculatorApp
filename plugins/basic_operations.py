import logging

# Define a basic_operations plugin
def execute(command, history_manager):
    """
    Execute arithmetic operations based on the command.
    
    Args:
        command (str): The user command from the REPL.
        history_manager (HistoryManager): Instance for managing calculation history.
    
    Returns:
        float: The result of the operation.
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Parse the command (e.g., "add 3 4")
        parts = command.split()
        if len(parts) != 3:
            raise ValueError("Invalid command format. Use: [operation] [num1] [num2].")
        
        operation = parts[0]
        num1 = float(parts[1])
        num2 = float(parts[2])
        
        # Perform the operation
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        # Log the operation and store it in history
        logger.info(f"Performed {operation} on {num1} and {num2}: {result}")
        history_manager.add_to_history(operation, num1, num2, result)
        
        return result
    
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        raise
    except ZeroDivisionError as zde:
        logger.error(f"ZeroDivisionError: {zde}")
        raise