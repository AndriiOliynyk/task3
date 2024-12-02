from elasticsearch import Elasticsearch
import json
from fastapi import APIRouter


router = APIRouter(tags=['Створює базу даних з рапортами'])
@router.get("/init-raports")
def create_database():

    API_KEY = "ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw=="

    with open("./src/1.json", "r") as f:
        data = json.load(f)

    client = Elasticsearch(
        "https://e060d5b03e824ef4b2ac8d3b655d5ae4.us-central1.gcp.cloud.es.io:443",
        api_key="ekx5d2hwTUJvdkFVVmduLTU4ZGI6R1F3V093bGRRdXU0X3pWN1ZnOGh4Zw=="
    )


    responce = client.create(index='raports_1', id='raports-doc1',body={})
    print(responce)