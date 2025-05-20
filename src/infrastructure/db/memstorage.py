from src.adapters.repository.interface import IStorageRepository
from src.domain.entities import ShortUrl


class MemStorageRepository(IStorageRepository):
    """Implementation of the repository based on pure python dict and store it in memory.

    NOT THREAD-SAFE
    """

    def __init__(self) -> None:  # noqa: D107
        self.storage: dict[str, ShortUrl] = {}

    def get_by_code(self, code: str) -> ShortUrl:
        """Return short url from given code"""
        return self.storage[code]

    def save(self, data: ShortUrl) -> None:
        """Save given short url"""
        self.storage[data.short_url] = data
