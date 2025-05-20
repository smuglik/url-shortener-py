from abc import ABC, abstractmethod

from src.domain.entities import ShortUrl


class IStorageRepository(ABC):
    """Abstract class for the storage repository"""

    @abstractmethod
    def save(self, short_url: ShortUrl) -> None:
        """Implement it in subclass"""
        raise NotImplementedError()

    @abstractmethod
    def get_by_code(self, code: str) -> ShortUrl:
        """Implement it in subclass"""
        raise NotImplementedError()
