import logging
import logging.handlers
import sys

from src.api_template.settings import settings

formatter = logging.Formatter(settings.logs_format)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(settings.logs_level)
stream_handler.setFormatter(formatter)

file_handler = logging.handlers.RotatingFileHandler(
    settings.logs_filename,
    maxBytes=settings.logs_max_bytes,
    backupCount=settings.logs_backup_count,
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logging.basicConfig(level=settings.logs_level, handlers=[stream_handler, file_handler])


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
