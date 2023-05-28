from enum import Enum
from starlette.responses import HTMLResponse
from uuid import UUID
from pydantic import BaseSettings
from fastapi import Path
from pydantic.main import BaseModel
from pydantic.networks import HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class To(BaseModel):
    name: str
    phone: str
    acct_number: str
    amount: float

class BMU_Config(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    bdb_url: str = "sqlite:///./bdb.db"

    class Config:
        env_file = ".env"


class BMU_Details(str, Enum):  # using for tags in bwroline
    user_id: UUID
    bwr = "bwroline.com",
    shd = "shamudoents.com",
    ghlp = "ghlp.com",
    egb = "ecwagoodnewsbwr.com.com",
    btgs = "btgees.com"


class BMU_Detail(BaseModel):
    key: str
    size: float | None = None
    click: int
    tags: list[str | None] = None
    is_active: bool
    name: str
    website: (str | None) = None


class Details(BaseModel):
    name: str
    pass
