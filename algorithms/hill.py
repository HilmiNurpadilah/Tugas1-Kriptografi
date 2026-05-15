"""
Modul Hill Cipher (2x2 dan 3x3)
"""
import numpy as np

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % modulus, modulus)
    if det_inv is None:
        return None
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    ) % modulus
    return matrix_modulus_inv

def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join([chr(n % 26 + ord('A')) for n in numbers])

def pad_text(text, size):
    text = ''.join([c for c in text if c.isalpha()])
    while len(text) % size != 0:
        text += 'X'
    return text

def hill_encrypt(text, key_matrix):
    steps = []
    n = key_matrix.shape[0]
    text = pad_text(text, n)
    nums = text_to_numbers(text)
    result = ''
    steps.append(f"Padding supaya kelipatan {n}: {text}")
    steps.append(f"Huruf ke angka: {nums}")
    steps.append(f"Matriks kunci: {key_matrix.tolist()}")
    for i in range(0, len(nums), n):
        block = np.array(nums[i:i+n])
        enc_block = np.dot(key_matrix, block) % 26
        steps.append(
            f"Blok {block.tolist()} × kunci → {enc_block.tolist()} → {numbers_to_text(enc_block)}"
        )
        result += numbers_to_text(enc_block)
    return result, steps, text

def hill_decrypt(text, key_matrix):
    steps = []
    n = key_matrix.shape[0]
    nums = text_to_numbers(text)
    result = ''
    inv_matrix = matrix_mod_inv(key_matrix, 26)
    if inv_matrix is None:
        return None, ["Kunci tidak memiliki invers modulo 26."], text
    steps.append(f"Huruf cipher ke angka: {nums}")
    steps.append(f"Matriks invers kunci: {inv_matrix.tolist()}")
    for i in range(0, len(nums), n):
        block = np.array(nums[i:i+n])
        dec_block = np.dot(inv_matrix, block) % 26
        steps.append(
            f"Blok {block.tolist()} × inv_kunci → {dec_block.tolist()} → {numbers_to_text(dec_block)}"
        )
        result += numbers_to_text(dec_block)
    return result, steps, text
