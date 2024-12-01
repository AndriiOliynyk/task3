import json
from fastapi import APIRouter

router = APIRouter(tags=['Має виводити CVE в яких knownRansomwareCampaignUse - Known, максимум 10'])

@router.get("/get/know")
def main():
    with open("./src/1.json", "r") as f:
        data = json.load(f)
    cve = []
    # перевірка чи по полі know.... є value 'Know'
    for i in data['vulnerabilities']:
        if i['knownRansomwareCampaignUse'] == 'Known':
            cve.append(i)
    
        if len(cve) == 10:
            break
    
    return cve