from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.adapters.repository.interface import IAsyncStorageRepository
from src.domain.entities import ShortUrl
from src.infrastructure.db.models import UrlModel


class SqlAlchemyStorage(IAsyncStorageRepository):
    """Implement storage based on SQLAlchemy."""

    def __init__(self, session: AsyncSession) -> None:  # noqa: D107
        self.session = session

    async def save(self, url: ShortUrl) -> None:
        """Save a short url to db."""
        model = UrlModel(short_code=url.short_url, original=url.original_url, created=url.created_at)
        self.session.add(model)
        await self.session.commit()

    async def get_by_code(self, code: str) -> ShortUrl:
        """Get short url by code."""
        result = await self.session.execute(select(UrlModel).where(UrlModel.short_code == code))
        model = result.scalar_one_or_none()
        if not model:
            raise ValueError(f"Invalid short code {code}")
        return ShortUrl(original_url=model.original, short_url=model.short_code, created_at=model.created)
