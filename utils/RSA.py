from random import randint
from typing import Tuple, List


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e: int, phi: int) -> int:
    def egcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, y = egcd(e, phi)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    else:
        return x % phi


def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise "Оба числа должны быть простыми"
    elif p == q:
        raise "Числа должны быть разными"
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randint(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    public_key = (n, e)
    private_key = (n, d)
    return (public_key, private_key)


def encrypt(public_key: Tuple[int, int], plaintext: str) -> str:
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return str(ciphertext)


def decrypt(private_key: Tuple[int, int], ciphertext: List[int]) -> str:
    n, d = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)
