from fastapi import APIRouter
from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
    api_key="ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw==",
    verify_certs=True
)

router = APIRouter(tags=["raports_database"])

@router.get("/get/raports")
def main():
    query = {
        "query": {
            "match_all": {}
        }
    }

    response = client.search(index="raports_1", body=query)

    results = [doc['_source'] for doc in response['hits']['hits']]
    return results