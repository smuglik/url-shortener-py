from fastapi import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.adapters.repository.interface import IAsyncStorageRepository
from src.application.use_case import UrlShortenerUseCase
from src.infrastructure.db.repo import SqlAlchemyStorage
from src.infrastructure.db.session import get_db


async def get_repository(session: AsyncSession = Depends(get_db)) -> IAsyncStorageRepository:
    """Return relevant storage repository"""
    return SqlAlchemyStorage(session=session)


async def get_service(repo: IAsyncStorageRepository = Depends(get_repository)) -> UrlShortenerUseCase:
    """Return use case"""
    return UrlShortenerUseCase(repo)
