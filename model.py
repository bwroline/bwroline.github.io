from typing import List, Optional
from pydantic import BaseModel  # Field


class bwr(BaseModel):
    id: List[int] = None
    email_id: Optional[List[str]] = None
    password: Optional[List[str]]
    name: Optional[str] = [Field(...), None]
    rate: Optional[float] = None
    tax: Optional[float] = None
    link: Optional[str] = None
    description: Optional[str] = None
    details: List[str] = None
    response: Optional[str] = None
    contents: Optional[str] = None


class HTM(BaseModel):
    def __init__(self):
        self.id: Optional[int]
        self.HTMLResponse: Optional[str] = None
        self.GET: Optional[str] = None
        self.HTMLResponse: Optional[str] = None


class usr(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    password: str = None
    password_again: str = None
    username: Optional[str] = None
    bdb: Optional[List[str]] = None
    response: Optional[str] = [HTM, None]


class BMU(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email_add: Optional[str] = None
    daily_income: Optional[float] = None
    monthly_salary: Optional[float] = None


bmu = {
    "id": [0, 1, 3, 4, 5],
    "email_id": [""],
    "password": [""],
    "name": "BWAYA MEDIA UNIT",
    "rate": 5.66556e65,
    "tax": 5.66556e6,
    "link": "",
    "description": "",
    "details": [""],
    "response": "",
    "contents": "txt/html/xml/application"
}
shd = {
    "id": [0, 1],
    "email_id": [""],
    "password": [""],
    "name": "shamudoents.com",
    "rate": 5.66556e65,
    "tax": 1.56655e6,
    "link": "",
    "description": "",
    "details": [""],
    "response": "",
    "contents": "txt/html/xml/application"
}
ghlp = {
    "id": [0, 2],
    "email_id": [""],
    "password": [""],
    "name": "great hussein legal practitioners",
    "rate": 5.66556e65,
    "tax": 1.56655e6,
    "link": "",
    "description": "",
    "details": [""],
    "response": "",
    "contents": "txt/html/xml/application"
}
egb = {
    "id": [0, 3],
    "email_id": [""],
    "password": [""],
    "name": "ecwa goodnews church Bwari Abuja",
    "rate": 5.66556e65,
    "tax": 1.56655e6,
    "link": "",
    "description": "",
    "details": [""],
    "response": "",
    "contents": "txt/html/xml/application"
}
btg = {
    "id": [0, 4],
    "email_id": [""],
    "password": [""],
    "name": "btgees.com",
    "rate": 5.66556e65,
    "tax": 1.56655e6,
    "link": "",
    "description": "",
    "details": [""],
    "response": "",
    "contents": "txt/html/xml/application"
}

bm = bwr(**bmu)
sh = bwr(**shd)
gh = bwr(**ghlp)
eg = bwr(**egb)
bt = bwr(**btg)

# To deploy my app at deta!
# use deta deploy

user = {
    "id": 6,
    "username": """<p>input(["\n email: ", "\n password: ", "\n password again: "])</p>""",
    "\n bdb": [987654321, 5.66556e65, 0, 1],
    "requests": []
}

users = range(0, 1, 9)
username = usr(**user)
