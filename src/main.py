from fastapi import FastAPI
from endpoint import info
from endpoint import get_all


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(info.router)
app.include_router(get_all.router)