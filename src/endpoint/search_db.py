from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
    api_key="ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw==",
    verify_certs=True
)

router = APIRouter(tags=["critical_cve"])

@router.get("/get")
def search_cve(query: str = Query(..., description="Search query for CVE")):
    body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["cveID","vulnerabilityName","shortDescription","product","notes"]
                }
            }
        }
    
    response = client.search(index="test_index5", body=body)

    results = [doc['_source'] for doc in response['hits']['hits']]

    cve = []
    for doc in results:
        if 'vulnerabilities' in doc:  
            for vuln in doc['vulnerabilities']:
                cve.append(vuln)

    update_response = client.update(
        index="raports_1",
        id="raports-doc1",
        doc={"cve_list": cve}
    )

    return response
