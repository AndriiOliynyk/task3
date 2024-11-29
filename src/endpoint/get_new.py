import json
from fastapi import APIRouter

router = APIRouter(tags=['Last 10 CVEs'])

@router.get("/get/new")
def main():
    with open("./src/1.json", "r") as f:
        data = json.load(f)
    cve = []
    
    for i in data['vulnerabilities']:
        cve.append(i)
        
        if len(cve) == 10:
            break

    return cve