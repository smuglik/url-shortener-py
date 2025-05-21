from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def init(app: FastAPI) -> None:
    """Do pre-start steps and then gracefully exit"""
