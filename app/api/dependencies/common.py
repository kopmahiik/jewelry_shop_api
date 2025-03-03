from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db.session import async_engine


async def get_session():
    Session = async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
    )

    async with Session() as session:
        yield session
