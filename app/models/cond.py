from pydantic import BaseModel


class ConditionsParam(BaseModel):
    name1: str
    name2: str


class Conditions(BaseModel):
    can: list[ConditionsParam] | list
    cannot: list[ConditionsParam] | list