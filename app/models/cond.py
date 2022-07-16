from fastapi import Body
from pydantic import BaseModel


class CondititionsBody(BaseModel):
    can: list[dict[str, str]] = Body(None, description="can conditions for combintions")
    cannot: list[dict[str, str]] = Body(
        None, description="cannot conditions for combintions"
    )
