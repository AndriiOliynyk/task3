import json
from fastapi import APIRouter

router = APIRouter(tags=['All cve 5 days'])

@router.get("/get/all")
def all_cve():
    with open("./src/1.json", "r") as f:
        data = json.load(f)
    cve = []
    
    last_5_days = ["2024-11-21", "2024-11-20", "2024-11-19", "2024-11-18", "2024-11-17"]
    
    for i in data['vulnerabilities']:
        if i['dateAdded'] in last_5_days:
            cve.append(i)
        
        if len(cve) == 40:
            break

    return cve