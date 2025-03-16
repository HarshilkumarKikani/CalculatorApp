import pytest
from plugins import basic_operations
from history.history_manager import HistoryManager
from plugins.statistics_operations import execute
from statistics import StatisticsError

@pytest.fixture
def history_manager():
    return HistoryManager()

def test_add_operation(history_manager):
    result = basic_operations.execute("add 2 3", history_manager)
    assert result == 5

def test_subtract_operation(history_manager):
    result = basic_operations.execute("subtract 10 4", history_manager)
    assert result == 6

def test_multiply_operation(history_manager):
    result = basic_operations.execute("multiply 3 7", history_manager)
    assert result == 21

def test_divide_operation(history_manager):
    result = basic_operations.execute("divide 8 2", history_manager)
    assert result == 4

def test_divide_by_zero(history_manager):
    with pytest.raises(ZeroDivisionError):
        basic_operations.execute("divide 5 0", history_manager)

def test_invalid_command(history_manager):
    with pytest.raises(ValueError):
        basic_operations.execute("invalid 2 3", history_manager)

def test_mean_operation(history_manager):
    result = execute("mean 1 2 3", history_manager)
    assert result == 2

def test_median_operation(history_manager):
    result = execute("median 1 2 3", history_manager)
    assert result == 2

def test_mode_operation(history_manager):
    result = execute("mode 2 2 3", history_manager)
    assert result == 2

def test_invalid_statistics_command(history_manager):
    with pytest.raises(ValueError):
        execute("invalid 1 2 3", history_manager)

def test_mode_statistics_error(history_manager):
    with pytest.raises(StatisticsError):
        execute("mode 1 1 2 2", history_manager)


