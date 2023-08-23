from utils.gamming import encrypt
from fastapi import APIRouter

router = APIRouter(tags=["gamming"])


@router.get("/gamming/encrypt", response_model=str)
def encrypt_gamming(text: str, gamma: str):
    return encrypt(text=text, gamma=gamma)
