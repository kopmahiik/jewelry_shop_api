import datetime
import decimal

from pydantic import BaseModel


class ProductResponseSchema(BaseModel):
    id: int
    title: str
    description: str | None
    price: decimal.Decimal
    image_path: str | None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class ProductCreateSchema(BaseModel):
    title: str
    description: str | None
    price: decimal.Decimal
    image_path: str | None

    class Config:
        from_attributes = True


class ProductUpdateSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    price: decimal.Decimal | None = None
    image_path: str | None = None

    class Config:
        from_attributes = True
