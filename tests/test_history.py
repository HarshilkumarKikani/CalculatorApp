import os
import pytest
import tempfile
from history.history_manager import HistoryManager

@pytest.fixture
def history_manager():
    return HistoryManager()

@pytest.fixture
def temp_history_file():
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        yield temp_file.name  # Pass the temp file name to the test
    os.remove(temp_file.name)  # Clean up after the test

def test_save_and_load_history(history_manager, temp_history_file):
    history_manager.filepath = temp_history_file  # Assign the temp file path
    history_manager.add_to_history("add", 3, 4, 7)
    history_manager.save_history()
    history_manager.load_history()
    assert len(history_manager.history) == 1
    assert history_manager.history.iloc[0]["Result"] == 7
