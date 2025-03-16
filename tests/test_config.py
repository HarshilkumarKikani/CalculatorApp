from utils.config import Config
import os

def test_config_custom_history_file():
    os.environ["HISTORY_FILE"] = "test_history.csv"
    config = Config()
    assert config.history_file == "test_history.csv"
    del os.environ["HISTORY_FILE"]  # Cleanup after the test

def test_config_default_history_file():
    if "HISTORY_FILE" in os.environ:
        del os.environ["HISTORY_FILE"]
    config = Config()
    assert config.history_file == "history.csv"  # Default value

def test_config_empty_env_variable():
    os.environ["HISTORY_FILE"] = ""  # Set to an empty string
    config = Config()
    assert config.history_file == "history.csv"  # Falls back to default
    del os.environ["HISTORY_FILE"]