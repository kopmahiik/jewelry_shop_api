from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from app.settings.config import settings

async_engine = AsyncEngine(
    create_engine(
        url=settings.DATABASE_URL
    )
)

async def get_db_session() -> AsyncSession:
    Session = async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
    )

    async with Session() as session:
        yield session
