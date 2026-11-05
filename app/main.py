from fastapi import FastAPI

from app import __version__
from app.config import Settings, get_settings
from app.db import Base, Database
from app.routers import health, items


def create_app(settings: Settings | None = None, database: Database | None = None) -> FastAPI:
    settings = settings or get_settings()
    database = database or Database(settings.database_url)
    Base.metadata.create_all(database.engine)
    app = FastAPI(title=settings.app_name, version=__version__)
    app.state.db = database
    app.include_router(health.router)
    app.include_router(items.router, prefix="/api/v1")
    return app
