from __future__ import annotations

import sys
from enum import Enum

from loguru import logger as _logger
from loguru._logger import Logger


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


def get_logger() -> Logger:
    from .settings import Settings  # noqa: PLC0415 — deferred to break circular import

    _logger.remove()
    _logger.add(
        sys.stdout,
        level=Settings.log_level.value,
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        enqueue=True,
    )
    return _logger  # type: ignore[return-value]


logger = get_logger()
