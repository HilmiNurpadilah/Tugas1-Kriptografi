"""
Modul Caesar Cipher
"""

def caesar_encrypt(text, key):
    steps = []
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            num = ord(char) - base
            enc = (num + key) % 26
            enc_char = chr(enc + base)
            steps.append(f"{char} jadi {num}. Rumus: (p + k) mod 26 = ({num} + {key}) mod 26 = {enc}. Jadi {enc_char}.")
            result += enc_char
        else:
            result += char
    return result, steps

def caesar_decrypt(text, key):
    steps = []
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            num = ord(char) - base
            dec = (num - key) % 26
            dec_char = chr(dec + base)
            steps.append(f"{char} jadi {num}. Rumus: (p - k) mod 26 = ({num} - {key}) mod 26 = {dec}. Jadi {dec_char}.")
            result += dec_char
        else:
            result += char
    return result, steps
