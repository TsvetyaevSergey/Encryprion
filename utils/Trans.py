def encrypt_transposition(plaintext, key):
    ciphertext = [''] * key
    for column in range(key):
        current_index = column
        while current_index < len(plaintext):
            ciphertext[column] += plaintext[current_index]
            current_index += key
    return ''.join(ciphertext)
