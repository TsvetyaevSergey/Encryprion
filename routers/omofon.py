from utils.omofon import homophonic_encryption
from fastapi import APIRouter

router = APIRouter(tags=["homophonic"])


@router.get("/homophonic/encrypt", response_model=str)
def encrypt_homophonic(text: str):
    return homophonic_encryption(input_text=text,)
