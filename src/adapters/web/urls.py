from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from src.adapters.web.deps import get_service
from src.adapters.web.handlers import get_original_url, get_short_url
from src.adapters.web.structs import ShortUrl, Url
from src.application.use_case import UrlShortenerUseCase


router = APIRouter()


@router.post("/shorten")
async def shorten(body: Url, service: UrlShortenerUseCase = Depends(get_service)) -> ShortUrl:
    """Get url and return shortened url"""
    return await get_short_url(body.url, service)


@router.get("/get-full-path")
async def get_full_path(short_code: str, service: UrlShortenerUseCase = Depends(get_service)) -> RedirectResponse:
    """Get code and redirect to original url"""
    original = await get_original_url(short_code, service)
    return RedirectResponse(url=original)
