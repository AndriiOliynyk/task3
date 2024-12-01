import json
from fastapi import APIRouter

router = APIRouter(tags=['All cve 5 days'])
# прописана адреса за якою висить фукція та відкритя файлу
@router.get("/get/all")
def all_cve():
    with open("./src/1.json", "r") as f:
        data = json.load(f)
    cve = []

    # це мій варіант як задати останні 5 днів оскільки вони статичні 
    days = "2024-11-"
    all_days = [] 

    for i in range(17, 22):
        day = days + str(i)  
        all_days.append(day) 
    # і сам пошук по json файлу якщо доходить до 40свє то більше не записує 
    for i in data['vulnerabilities']:
        if i['dateAdded'] in all_days:
            cve.append(i)
        
        if len(cve) == 40:
            break

    return cve