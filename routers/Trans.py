from utils.Trans import encrypt_transposition
from fastapi import APIRouter

router = APIRouter(tags=["Trans"])


@router.get("/Trans/encrypt", response_model=str)
def transposition(text: str, key: int):
    return encrypt_transposition(key=key, plaintext=text)
