from utils.RSA import generate_keypair, encrypt
from fastapi import APIRouter

router = APIRouter(tags=["RSA"])


@router.get("/RSA/encrypt", response_model=str)
def encrypt_RSA(text: str, p: int, q: int):
    public, private = generate_keypair(p, q)
    return encrypt(public_key=public, plaintext=text)