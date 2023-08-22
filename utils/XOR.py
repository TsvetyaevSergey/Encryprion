def xor_encrypt(plaintext):
    key = "asdada"
    ciphertext = ""
    for i in range(len(plaintext)):
        char = chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
        ciphertext += char
    return ciphertext
