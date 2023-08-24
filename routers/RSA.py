from utils.RSA import generate_keypair, encrypt
from fastapi import APIRouter
from utils.RSA import is_prime
router = APIRouter(tags=["RSA"])


@router.get("/RSA/encrypt", response_model=str)
def encrypt_RSA(text: str, p: int, q: int):
    if not (is_prime(p) and is_prime(q)):
        return "Оба числа должны быть простыми"
    elif p == q:
        return "Числа должны быть разными"
    public, private = generate_keypair(p, q)
    return encrypt(public_key=public, plaintext=text)
