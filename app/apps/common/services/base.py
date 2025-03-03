from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, desc


class BaseService:
    model = None

    @classmethod
    async def get_item_list(cls, session: AsyncSession, **filters):
        query = select(cls.model).filter_by(**filters)
        result = await session.execute(query)
        return result


