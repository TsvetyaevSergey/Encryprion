def caesar_cipher(text, key):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if char.isalpha():
      num = ord(char)
      if char.islower():
        base = ord('a')
      else:
        base = ord('A')
      num = (num - base + key) % 26 + base
      result += chr(num)
    else:
      result += char
  return result