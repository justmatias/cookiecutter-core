from collections.abc import Generator

from {{ cookiecutter.module_name }}.utils import logger


def test_log(
    capture_logs: Generator[list[str]], log_level: str, message: str
) -> None:
    logger.log(log_level, message)
    logs = list(capture_logs)
    assert message in logs[0]
    assert log_level in logs[0]
