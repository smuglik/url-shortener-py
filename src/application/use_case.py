from datetime import UTC, datetime

from src.adapters.repository.interface import IAsyncStorageRepository
from src.domain.entities import ShortUrl
from src.domain.rules import UrlShortenerRule


class UrlShortenerUseCase:
    """Implementation of the UrlShortenerUseCase"""

    def __init__(self, repository: IAsyncStorageRepository) -> None:
        """Construct a new UrlShortenerUseCase"""
        self.repo = repository

    async def create_short_url(self, original_url: str) -> ShortUrl:
        """Create a new short url from an original url"""
        short_code = UrlShortenerRule().generate_short_url()
        short_url = ShortUrl(original_url, short_code, datetime.now(tz=UTC))
        await self.repo.save(short_url)
        return short_url

    async def get_original_url(self, short_code: str) -> str:
        """Get the original url from the short url"""
        short_url = await self.repo.get_by_code(short_code)
        return short_url.original_url
