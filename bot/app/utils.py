import logging
import os
from datetime import datetime
from pydantic_core import core_schema
from logging.handlers import RotatingFileHandler


def setup_logging(log_level: str, logging_path: str):
    logger = logging.getLogger()
    logger.setLevel(log_level)
    handler = RotatingFileHandler(os.path.join(logging_path, 'app.log'), maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
                              "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def fmt_date(d: datetime):
    return d.strftime('%d.%m.%Y в %H:%M')
