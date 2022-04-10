from pydantic import BaseModel


class Parameters(BaseModel):
    name1: list[str]
    name2: list[str]