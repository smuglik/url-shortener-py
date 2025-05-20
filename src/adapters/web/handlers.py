from src.adapters.web.structs import ShortUrl
from src.application.use_case import UrlShortenerUseCase


def get_short_url(url: str, service: UrlShortenerUseCase) -> ShortUrl:  # noqa: D103
    short = service.create_short_url(url)
    return ShortUrl.from_orm(short)
