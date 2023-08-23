import string


def encrypt(text, gamma):
    textLen = len(text)
    gammaLen = len(gamma)
    alphabet = list(string.ascii_lowercase)
    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])

    code = []
    for i in range(textLen):
        code.append(alphabet[(alphabet.index(text[i]) + alphabet.index(keyText[i])) % 26])

    return code
