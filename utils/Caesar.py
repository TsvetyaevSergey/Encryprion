def caesar_cipher(text:str, key:str):
  newkey = int(key)
  result = ""
  for i in range(len(text)):
    char = text[i]
    if char.isalpha():
      num = ord(char)
      if char.islower():
        base = ord('a')
      else:
        base = ord('A')
      num = (num - base + newkey) % 26 + base
      result += chr(num)
    else:
      result += char
  return result