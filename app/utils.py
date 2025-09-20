import logging
import os

from logging.handlers import RotatingFileHandler
from app.config import config


def setup_logging(level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(level)
    handler = RotatingFileHandler(os.path.join(config.logging_path, 'app.log'), maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
                              "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
