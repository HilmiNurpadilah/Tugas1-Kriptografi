"""
Modul Affine Cipher
"""

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    steps = []
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            num = ord(char) - base
            enc = (a * num + b) % 26
            enc_char = chr(enc + base)
            steps.append(f"{char}={num}. Rumus: (a·p + b) mod 26 = ({a}×{num}+{b}) mod 26 = {enc}. Jadi {enc_char}.")
            result += enc_char
        else:
            result += char
    return result, steps

def affine_decrypt(text, a, b):
    steps = []
    result = ''
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None, ["Tidak ada invers dari a modulo 26."]
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            num = ord(char) - base
            dec = (a_inv * (num - b)) % 26
            dec_char = chr(dec + base)
            steps.append(f"{char}={num}. Invers a = {a_inv}. Rumus: a⁻¹(p - b) mod 26 = {a_inv}×({num}-{b}) mod 26 = {dec}. Jadi {dec_char}.")
            result += dec_char
        else:
            result += char
    return result, steps
