from fastapi import Depends
from src.adapters.repository.interface import IStorageRepository
from src.application.use_case import UrlShortenerUseCase
from src.infrastructure.db.memstorage import MemStorageRepository


def get_repository() -> IStorageRepository:
    """Return relevant storage repository"""
    return MemStorageRepository()


def get_service(repo: IStorageRepository = Depends(get_repository)) -> UrlShortenerUseCase:
    """Return use case"""
    return UrlShortenerUseCase(repo)
