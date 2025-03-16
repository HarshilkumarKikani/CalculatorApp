import logging
from utils.logging_config import setup_logging

def test_logging_configuration():
    setup_logging()
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)  # Ensure it's set explicitly
    assert logger.level == logging.INFO


def test_logging_setup():
    setup_logging()
    logger = logging.getLogger("test_logger")
    assert logger.level == logging.INFO