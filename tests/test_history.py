import os
import pandas as pd
import pytest
from history.history_manager import HistoryManager

@pytest.fixture
def history_manager():
    # Create a fresh instance of HistoryManager for each test
    manager = HistoryManager()
    yield manager
    # Cleanup: Remove test history file if created
    if os.path.exists(manager.filepath):
        os.remove(manager.filepath)

def test_add_to_history(history_manager):
    history_manager.add_to_history("add", 3, 4, 7)
    assert len(history_manager.history) == 1
    assert history_manager.history.iloc[0]["Operation"] == "add"
    assert history_manager.history.iloc[0]["Result"] == 7

def test_display_history(history_manager):
    history_manager.add_to_history("multiply", 5, 2, 10)
    history_output = history_manager.display_history()
    assert "multiply" in history_output
    assert "10" in history_output

def test_save_and_load_history(history_manager):
    history_manager.add_to_history("subtract", 8, 3, 5)
    history_manager.save_history()

    # Create a new manager and load the history
    new_manager = HistoryManager()
    new_manager.load_history()
    assert len(new_manager.history) == 1
    assert new_manager.history.iloc[0]["Result"] == 5

def test_clear_history(history_manager):
    history_manager.add_to_history("divide", 10, 2, 5)
    history_manager.clear_history()
    assert history_manager.history.empty