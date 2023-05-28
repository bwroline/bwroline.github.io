from starlette.responses import HTMLResponse
from typing import Union
# import bom.BMU_Detail, boHTML
# from fastapi import FastAPI

# b = FastAPI()


def r_b(q: Union[str, HTMLResponse, None] = None):
    #b_d=bom.BMU_Detail:
    bwr = {"id": b_d.name, "html/text": boHTML.bwr_, "bwr": b_b.name}
    if q:
        bwr.update({"q": q})