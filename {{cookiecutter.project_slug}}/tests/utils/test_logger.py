from collections.abc import Generator

from {{ cookiecutter.module_name }}.utils import LogLevel, logger


def test_log(
    capture_logs: Generator[list[str]], log_level: LogLevel, message: str
) -> None:
    logger.log(log_level.value, message)
    logs = list(capture_logs)
    assert message in logs[0]
    assert log_level.name in logs[0]
