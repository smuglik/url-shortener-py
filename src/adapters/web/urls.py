from fastapi import APIRouter, Depends
from src.adapters.web.deps import get_service
from src.adapters.web.handlers import get_short_url
from src.adapters.web.structs import ShortUrl, Url
from src.application.use_case import UrlShortenerUseCase


router = APIRouter()


@router.post("/shorten")
async def shorten(body: Url, service: UrlShortenerUseCase = Depends(get_service)) -> ShortUrl:
    """Get url and return shortened url"""
    return get_short_url(body.url, service)
