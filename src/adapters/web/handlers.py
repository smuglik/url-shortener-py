from src.adapters.web.structs import ShortUrl
from src.application.use_case import UrlShortenerUseCase


async def get_short_url(url: str, service: UrlShortenerUseCase) -> ShortUrl:  # noqa: D103
    short = await service.create_short_url(url)
    return ShortUrl.model_validate(short)


async def get_original_url(short_code: str, service: UrlShortenerUseCase) -> str:  # noqa: D103
    original = await service.get_original_url(short_code)
    return original
