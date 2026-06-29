from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .logger import LogLevel


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    log_level: LogLevel = Field(default=LogLevel.DEBUG)


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()


Settings = get_settings()
