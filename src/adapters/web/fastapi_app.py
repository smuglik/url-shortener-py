from fastapi import FastAPI
from src.adapters.web.urls import router


def create_app() -> FastAPI:
    """Create the FastAPI app"""
    app = FastAPI()
    app.include_router(router)
    return app
