import sqlalchemy as sa

from sqlalchemy.orm.decl_api import declarative_base


Base = declarative_base()


class TimedBaseModel(Base):
    __abstract__ = True

    created_at = sa.Column(sa.TIMESTAMP(timezone=True), server_default=sa.func.now())