
"""Зробив імпорти всього шо потрібно також роутери підєднав"""

from fastapi import FastAPI
from endpoint import info
from endpoint import get_all
from endpoint import get_new
from endpoint import get_know
from endpoint import search
from endpoint import elastic_app1
from endpoint import get_all_db
from endpoint import get_new_db


app = FastAPI()

@app.get("/") #корінь сайту
def root():
    return {"message": "Hello World"}


"""викликаю роутери"""
app.include_router(info.router)
app.include_router(get_all.router)
app.include_router(get_new.router)
app.include_router(get_know.router)
app.include_router(search.router)
app.include_router(elastic_app1.router)
app.include_router(get_all_db.router)
app.include_router(get_new_db.router)