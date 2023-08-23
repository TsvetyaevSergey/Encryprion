from utils.RSA import generate_keypair, encrypt
from fastapi import APIRouter

router = APIRouter(tags=["RSA"])


@router.get("/RSA/encrypt", response_model=str)
def encrypt_RSA(text: str, p: str, q: str):
    public, private = generate_keypair(int(p), int(q))
    return encrypt(public_key=public, plaintext=text)