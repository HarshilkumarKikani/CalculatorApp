import logging
import statistics

def execute(command, history_manager):
    """
    Execute statistical operations based on the command.

    Args:
        command (str): The user command from the REPL.
        history_manager (HistoryManager): Instance for managing calculation history.

    Returns:
        float: The result of the statistical operation.
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Parse the command (e.g., "mean 1 2 3")
        parts = command.split()
        if len(parts) < 2:
            raise ValueError("Invalid command format. Use: [operation] [numbers].")
        
        operation = parts[0]
        numbers = list(map(float, parts[1:]))  # Convert remaining arguments to floats
        
        # Perform the statistical operation
        if operation == "mean":
            result = statistics.mean(numbers)
        elif operation == "median":
            result = statistics.median(numbers)
        elif operation == "mode":
            result = statistics.mode(numbers)
        else:
            raise ValueError(f"Unknown statistical operation: {operation}")
        
        # Log the operation and store it in history
        logger.info(f"Performed {operation} on {numbers}: {result}")
        history_manager.add_to_history(operation, numbers, None, result)
        
        return result

    except statistics.StatisticsError as se:
        logger.error(f"StatisticsError: {se}")
        raise
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        raise