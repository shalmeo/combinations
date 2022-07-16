import sqlalchemy as sa

from app.database.base import TimedBaseModel


class Combination(TimedBaseModel):
    __tablename__ = "combinations"

    hash = sa.Column(sa.String, primary_key=True, unique=True)
    data = sa.Column(sa.JSON)
