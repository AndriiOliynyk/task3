
"""Зробив імпорти всього шо потрібно також роутери підєднав"""

from fastapi import FastAPI
from endpoint import info
from endpoint import get_all_db
from endpoint import get_new_db
from endpoint import get_know_db
from endpoint import search_db
from endpoint import elastic_app
from endpoint import elastic_raports
from endpoint import raports



app = FastAPI()

@app.get("/") #корінь сайту
def root():
    return {"message": "Hello World"}


"""викликаю роутери"""
app.include_router(info.router)
app.include_router(elastic_app.router)
app.include_router(get_all_db.router)
app.include_router(get_new_db.router)
app.include_router(get_know_db.router)
app.include_router(search_db.router)
app.include_router(elastic_raports.router)
app.include_router(raports.router)