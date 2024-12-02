from elasticsearch import Elasticsearch
import json

API_KEY = "ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw=="

with open("./src/1.json", "r") as f:
    data = json.load(f)

client = Elasticsearch(
    "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
    api_key="ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw=="
)


client.create(index='test_index1', id='test-doc',body=data)
# client.indices.create(index="test_index1")