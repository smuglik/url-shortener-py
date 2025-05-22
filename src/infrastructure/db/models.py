from datetime import datetime

from sqlalchemy import Index
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):  # noqa: D101
    id: Mapped[int] = mapped_column(primary_key=True)


class UrlModel(Base):  # noqa: D101
    __tablename__ = "urls"

    original: Mapped[str] = mapped_column(nullable=False)
    short_code: Mapped[str] = mapped_column(unique=True, nullable=False)
    created: Mapped[datetime] = mapped_column(default=datetime.now)

    __table_args__ = (Index("idx_urls_short_code", "short_code", postgresql_using="hash"),)
