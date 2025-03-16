from statistics import mean, median, StatisticsError
from collections import Counter

def execute(command, history_manager):
    parts = command.split()
    operation = parts[0]
    numbers = list(map(float, parts[1:]))
    result = None

    if operation == "mean":
        result = mean(numbers)
    elif operation == "median":
        result = median(numbers)
    elif operation == "mode":
        # Custom logic to handle ties
        counts = Counter(numbers)
        most_common = counts.most_common()
        max_frequency = most_common[0][1]
        modes = [num for num, freq in most_common if freq == max_frequency]
        if len(modes) > 1:
            raise StatisticsError("no unique mode; multiple equally common values")
        result = modes[0]
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    # Log the operation to history
    history_manager.add_to_history(operation, numbers, None, result)

    return result