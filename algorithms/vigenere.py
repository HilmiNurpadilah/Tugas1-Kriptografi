"""
Modul Vigenere Cipher
"""

def generate_key(text, key):
    key = list(key)
    if len(key) == len(text):
        return ''.join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vigenere_encrypt(text, key):
    steps = []
    key_full = generate_key(text, key)
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(key_full[i].upper()) - ord('A')
            num = ord(char) - base
            enc = (num + k) % 26
            enc_char = chr(enc + base)
            steps.append(f"{char}={num}, key {key_full[i]}={k}. Rumus: (p + k) mod 26 = ({num} + {k}) mod 26 = {enc}. Jadi {enc_char}.")
            result += enc_char
        else:
            result += char
    return result, steps, key_full

def vigenere_decrypt(text, key):
    steps = []
    key_full = generate_key(text, key)
    result = ''
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(key_full[i].upper()) - ord('A')
            num = ord(char) - base
            dec = (num - k) % 26
            dec_char = chr(dec + base)
            steps.append(f"{char}={num}, key {key_full[i]}={k}. Rumus: (p - k) mod 26 = ({num} - {k}) mod 26 = {dec}. Jadi {dec_char}.")
            result += dec_char
        else:
            result += char
    return result, steps, key_full
