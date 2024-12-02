from elasticsearch import Elasticsearch
import json
from fastapi import APIRouter

router = APIRouter(tags=['Створює базу даних'])

@router.get("/init-db1")
def create_database():

    API_KEY = "ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw=="

    with open("./src/1.json", "r") as f:
        data = json.load(f)

    client = Elasticsearch(
        "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
        api_key=API_KEY
    )

    index_name = 'test_index3'

    index_mapping = {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "catalogVersion": {"type": "keyword"},
                "dateReleased": {"type": "date"},
                "count": {"type": "integer"},
                "vulnerabilities": {
                    "type": "nested",
                    "properties": {
                        "cveID": {"type": "keyword"},
                        "vendorProject": {"type": "text"},
                        "product": {"type": "text"},
                        "vulnerabilityName": {"type": "text"},
                        "dateAdded": {"type": "date"},
                        "shortDescription": {"type": "text"},
                        "requiredAction": {"type": "text"},
                        "dueDate": {"type": "date"},
                        "knownRansomwareCampaignUse": {"type": "keyword"},
                        "notes": {"type": "text"},
                        "cwes": {"type": "keyword"}
                    }
                }
            }
        }
    }

    if not client.indices.exists(index=index_name):
        client.indices.create(index=index_name, body=index_mapping)
    
    response = client.index(index=index_name, document=data)
    print(response)

    return {"message": "Database initialized and data imported successfully"}
