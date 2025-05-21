from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src.infrastructure.confs.settings import get_settings


settings = get_settings()
engine = create_async_engine(url=settings.postgres_dsn.encoded_string(), echo=settings.db_echo)
session_local = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, Any]:
    """Генератор сессий для FastAPI Depends."""
    async with session_local() as session:
        yield session
