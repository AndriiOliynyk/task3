from fastapi import APIRouter
from elasticsearch import Elasticsearch

router = APIRouter(tags=["Останні 10"])

client = Elasticsearch(
    "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
    api_key="ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw==",
    verify_certs=True
)

@router.get("/get/know")
def main():
    response = client.search(
        index="test_index5",
        body={
            "query": {"term": {"knownRansomwareCampaignUse.keyword": "Known"}},
            "size": 10
        }
    )

    results = [doc['_source'] for doc in response['hits']['hits']]

    update_response = client.update(
        index="raports_1",
        id="raports-doc1",
        doc={"cve_list": results} 
    )

    return results
