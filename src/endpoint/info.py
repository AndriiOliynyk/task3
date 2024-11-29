from fastapi import APIRouter

router = APIRouter(tags=["info"])

@router.get("/info")
def print():
    # print("Json finder CVE \nDeveloper:AndriiOliynyk \nVersion:alpha \nPublished:29.11.2024 ")
    return("Json finder CVE \nDeveloper:AndriiOliynyk \nVersion:alpha \nPublished:29.11.2024 ")