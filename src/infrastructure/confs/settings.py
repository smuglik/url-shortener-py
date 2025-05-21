from functools import lru_cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):  # noqa: D101
    postgres_dsn: PostgresDsn
    db_echo: bool


@lru_cache
def get_settings() -> AppSettings:
    """Return settings instance."""
    return AppSettings()
