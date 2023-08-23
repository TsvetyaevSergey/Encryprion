from utils.Trans import encrypt_transposition
from fastapi import APIRouter

router = APIRouter(tags=["Trans"])


@router.get("/Trans/encrypt", response_model=str)
def encrypt_RSA(text: str, key: str):
    return encrypt_transposition(key=key, plaintext=text)
