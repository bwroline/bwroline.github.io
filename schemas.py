from typing import List, Union
from bom import BMU_Detail
from pydantic import BaseModel


class BwrolineBase(BaseModel):
    title: str
    description: str | None = None


class BwrolineCreate(BwrolineBase):
    pass


class Bwroline(BwrolineBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    bwr: List[Bwroline] = []
    update: BMU_Detail

    class Config:
        orm_mode = True
