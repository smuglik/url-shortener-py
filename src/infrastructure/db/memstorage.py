from src.adapters.repository.interface import IStorageRepository
from src.domain.entities import ShortUrl


###
# for testing purposes
storage = {}


class MemStorageRepository(IStorageRepository):
    """Implementation of the repository based on pure python dict and store it in memory.

    NOT THREAD-SAFE
    """

    def __init__(self) -> None:  # noqa: D107
        pass

    def get_by_code(self, code: str) -> ShortUrl:
        """Return short url from given code"""
        return storage[code]

    def save(self, data: ShortUrl) -> None:
        """Save given short url"""
        storage[data.short_url] = data
