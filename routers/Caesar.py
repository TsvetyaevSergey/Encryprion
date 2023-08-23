from utils.Caesar import caesar_cipher
from fastapi import APIRouter

router = APIRouter(tags=["caesar"])


@router.get("/caesar/encrypt", response_model=str)
def encrypt_caesar(text: str, key: int):
    return caesar_cipher(text=text, key=key)
