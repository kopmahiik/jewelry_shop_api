import datetime

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.sql import select, and_

class Base(DeclarativeBase):
    ...


class TimeStampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(sa.DateTime, default=sa.func.now(), nullable=True)
    updated_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime,
        default=sa.func.now(),
        onupdate=sa.func.now(),
        nullable=True
    )


class FlagsMixin:
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=True, nullable=False)
    is_deleted: Mapped[bool] = mapped_column(sa.Boolean, default=False, nullable=False)

    @classmethod
    def get_not_deleted(cls, session: Session):
        """Fetch only non-deleted records"""
        stmt = select(cls).where(cls.is_deleted == False)
        return session.scalars(stmt).all()

    @classmethod
    def get_active(cls, session: Session):
        stmt = select(cls).where(and_(cls.is_deleted == False, cls.is_active == True))
        return session.scalars(stmt).all()


class TimeStampFlagsMixin(TimeStampMixin, FlagsMixin):
    ...
