import logging
from utils.logging_config import setup_logging

def test_logging_configuration():
    setup_logging()
    logger = logging.getLogger(__name__)
    assert logger is not None