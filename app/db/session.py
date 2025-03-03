from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine

from app.settings.config import settings

async_engine = AsyncEngine(
    create_engine(
        url=settings.DATABASE_URL,
        echo=True
    )
)
