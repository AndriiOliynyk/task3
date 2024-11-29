from fastapi import FastAPI
from endpoint import info


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(info.router)