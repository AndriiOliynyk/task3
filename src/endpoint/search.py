from fastapi import APIRouter, Query
import json


router = APIRouter(tags=["critical_cve"])
@router.get("/get")

def print(query: str = Query):
    with open("./src/1.json", "r") as f:
        data = json.load(f)
    
    cve = []
    # я реалізував пошук по словах через query яке доступне в фаст апі 
    # як користуватися цим http://localhost:8000/get?key=value | наприклад /get?key=oracle
    for i in data["vulnerabilities"]:
        if any(query.lower() in str(value).lower() for value in i.values()):
            cve.append(i)

    return cve