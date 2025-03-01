import decimal

from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa

from app.apps.common.models import Base, TimeStampFlagsMixin


class Product(Base, TimeStampFlagsMixin):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(sa.String(255))
    description: Mapped[str | None] = mapped_column(sa.Text(), nullable=True)
    price: Mapped[decimal.Decimal] = mapped_column(sa.DECIMAL(12, 2), default=0)
    image_path: Mapped[str | None] = mapped_column(sa.String(length=255), nullable=True)

