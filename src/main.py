from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create initial application instance."""
    application = FastAPI()
    return application

app = create_app()

@app.get("/")
async def root() -> dict[str,str]:
    """Return welcome message."""
    return {"message": "Hello World"}
