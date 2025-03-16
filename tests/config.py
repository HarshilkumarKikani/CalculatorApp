from utils.config import Config
import os

def test_config_history_file():
    os.environ["HISTORY_FILE"] = "test_history.csv"
    config = Config()
    assert config.history_file == "test_history.csv"

def test_config_default():
    if "HISTORY_FILE" in os.environ:
        del os.environ["HISTORY_FILE"]
    config = Config()
    assert config.history_file == "history.csv"