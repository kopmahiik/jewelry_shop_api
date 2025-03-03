from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, insert

from app.apps.common.exceptions import ObjDoesNotExistException
from app.apps.products.models.products import Product


class ProductService:

    @classmethod
    async def get_product_list(cls, session: AsyncSession, **filters):
        query = select(Product).filter_by(**filters)
        result = await session.scalars(query)
        return result.all()

    @classmethod
    async def get_product(cls, session: AsyncSession, product_id: int) -> Product | None:
        query = select(Product).filter_by(id=product_id)
        result = await session.scalars(query)

        product = result.one_or_none()
        if not product:
            raise ObjDoesNotExistException
        return product

    @classmethod
    async def create_product(cls, session: AsyncSession, **data) -> Product:
        product = Product(**data)
        session.add(product)
        await session.commit()
        return product

    @classmethod
    async def update_product(cls, session: AsyncSession, product_id: int, **data) -> Product | None:
        product = await cls.get_product(session, product_id)

        for attr, value in data.items():
            setattr(product, attr, value)

        await session.commit()
        await session.refresh(product)
        return product

    @classmethod
    async def delete_product(cls, session: AsyncSession, product_id: int) -> None:
        product = await cls.get_product(session, product_id)

        await session.delete(product)
        await session.commit()


