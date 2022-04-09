from pydantic import BaseModel


class Conditions(BaseModel):
    can: list[dict[str, str]]
    cannot: list[dict[str, str]]