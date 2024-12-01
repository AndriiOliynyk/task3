from fastapi import APIRouter

router = APIRouter(tags=["info"])
# функція яка показує інформацію про програму
@router.get("/info")
def print():
    return("Json finder CVE Developer:AndriiOliynyk Version:alpha Published:29.11.2024")