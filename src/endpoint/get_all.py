import json
from fastapi import APIRouter

router = APIRouter(tags=['All cve 5 days'])

@router.get("/get/all")
def all_cve():
    with open("./src/1.json", "r") as f:
        data = json.load(f)
    cve = []


    days = "2024-11-"
    all_days = [] 

    for i in range(17, 22):
        day = days + str(i)  
        all_days.append(day) 
    
    for i in data['vulnerabilities']:
        if i['dateAdded'] in all_days:
            cve.append(i)
        
        if len(cve) == 40:
            break

    return cve