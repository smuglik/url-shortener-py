from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Url(BaseModel):  # noqa: D101
    url: str


class ShortUrl(Url):  # noqa: D101
    url: str = Field(..., alias="short_url")
    created_at: datetime = Field(..., alias="created_at")

    model_config = ConfigDict(from_attributes=True)
