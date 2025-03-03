from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.common import get_session
from app.api.schemas.products import ProductResponseSchema, ProductCreateSchema, ProductUpdateSchema
from app.apps.products.services.products import ProductService

router = APIRouter(prefix='/products', tags=['products'])


@router.get("/", response_model=list[ProductResponseSchema])
async def get_product_list(session: Annotated[AsyncSession, Depends(get_session)]):
    product_list = await ProductService.get_product_list(session)
    return product_list


@router.post("/", response_model=ProductResponseSchema)
async def create_product(
        product_data: ProductCreateSchema,
        session: Annotated[AsyncSession, Depends(get_session)]
):
    product = await ProductService.create_product(session, **product_data.model_dump())
    return product


@router.get("/{product_id}", response_model=ProductResponseSchema)
async def get_product(
        product_id: Annotated[int, Path],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    product = await ProductService.get_product(session, product_id)
    return product


@router.put("/{product_id}", response_model=ProductResponseSchema)
async def update_product(
        product_id: Annotated[int, Path],
        update_data: ProductUpdateSchema,
        session: Annotated[AsyncSession, Depends(get_session)]
):
    data = update_data.model_dump(exclude_unset=True)
    product = await ProductService.update_product(session, product_id, **data)
    print(product)
    return product
