from fastapi import FastAPI
from endpoint import info
from endpoint import get_all
from endpoint import get_new
from endpoint import get_know
from endpoint import search


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(info.router)
app.include_router(get_all.router)
app.include_router(get_new.router)
app.include_router(get_know.router)
app.include_router(search.router)