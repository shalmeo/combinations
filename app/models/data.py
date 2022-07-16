from pydantic import BaseModel
from fastapi import Body

from app.models.cond import CondititionsBody


class CombinationsBody(BaseModel):
    parameters: dict[str, list[str]] = Body(
        ..., description="parameters for combinations"
    )
    conditions: CondititionsBody = Body(None, description="conditions for combinations")
