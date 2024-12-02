from fastapi import APIRouter
from elasticsearch import Elasticsearch

router = APIRouter(tags=["Має виводити CVE в яких knownRansomwareCampaignUse - Known, максимум 10"])

client = Elasticsearch(
    "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
    api_key="ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw==",
    verify_certs=True
)

@router.get("/get/new")
def main():
    # Запит до Elasticsearch
    query = {
        "query": {
            "match_all": {}
        }
    }

    response = client.search(index="test_index2", body=query)

    # Отримання документів
    results = [doc['_source'] for doc in response['hits']['hits']]

    cve = []

    for doc in results:
        if 'vulnerabilities' in doc:
            for vuln in doc['vulnerabilities']:
                    cve.append(vuln)
                    if len(cve) == 10:
                        return cve

    update_response = client.update(
        index="raports_1",
        id="raports-doc1",
        doc={"cve_list": cve} 
    )

    return cve
