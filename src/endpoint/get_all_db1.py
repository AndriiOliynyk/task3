from fastapi import APIRouter
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta

router = APIRouter(tags=["Отримати CVE з 2024-11-20 до 2024-11-25"])

client = Elasticsearch(
    "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
    api_key="ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw==",
    verify_certs=True
)

@router.get("/get/all")
def main():
    end_date = "2024-11-25"

    start_date = (datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=5)).strftime("%Y-%m-%d")

    response = client.search(
        index="test_index5",
        body={
            "query": {
                "range": {
                    "dateAdded": {
                        "gte": start_date,
                        "lte": end_date,
                        "format": "yyyy-MM-dd"
                    }
                }
            },
            "size": 40 
        }
    )

    results = [doc['_source'] for doc in response['hits']['hits']]

    update_response = client.update(
        index="raports_1",
        id="raports-doc1",
        doc={"cve_list": results} 
    )
    return results