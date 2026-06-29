from __future__ import annotations

import sys
from enum import Enum

from loguru import logger as _logger
from loguru._logger import Logger
from .settings import Settings 

def get_logger() -> Logger:
    _logger.remove()
    _logger.add(
        sys.stdout,
        level="DEBUG",
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        enqueue=True,
    )
    return _logger  # type: ignore[return-value]


logger = get_logger()
