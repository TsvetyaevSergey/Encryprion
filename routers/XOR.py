from utils.XOR import xor_encrypt
from fastapi import APIRouter, HTTPException, status, Response, Request

router = APIRouter(tags=["XOR"])


@router.get("/XOR/encrypt", response_model=str)
def XOR(text: str, key: str):
    return xor_encrypt(plaintext=text, key=key)
