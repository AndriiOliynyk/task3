import json
from fastapi import APIRouter

router = APIRouter(tags=['Last 10 CVEs'])

@router.get("/get/new")
def main():
    with open("./src/1.json", "r") as f:
        data = json.load(f)
    
    # тут логіка як і get/all але просто обмеження на 10 cve тобто я проходжуся по всіх але вивожу тіки 10 
    cve = []
    for i in data['vulnerabilities']:
        cve.append(i)
        
        if len(cve) == 10:
            break

    return cve