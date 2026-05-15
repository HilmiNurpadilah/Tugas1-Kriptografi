"""
Aplikasi Web Simulasi Kriptografi Klasik
"""
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from algorithms import caesar, vigenere, affine, hill, playfair
import numpy as np


app = Flask(__name__)
app.secret_key = 'kriptografi2026'

ALGORITHMS = {
    'caesar': {
        'name': 'Caesar Cipher',
        'module': caesar,
        'key_label': 'Key (angka)',
        'key_type': 'number',
        'key_hint': '0-25',
    },
    'vigenere': {
        'name': 'Vigenere Cipher',
        'module': vigenere,
        'key_label': 'Key (teks)',
        'key_type': 'text',
        'key_hint': 'A-Z',
    },
    'affine': {
        'name': 'Affine Cipher',
        'module': affine,
        'key_label': 'Key a,b (misal: 5,8)',
        'key_type': 'text',
        'key_hint': 'a dan b dipisah koma',
    },
    'hill2': {
        'name': 'Hill Cipher 2x2',
        'module': hill,
        'key_label': 'Key 2x2 (4 angka, misal: 3,3,2,5)',
        'key_type': 'text',
        'key_hint': '4 angka dipisah koma',
    },
    'hill3': {
        'name': 'Hill Cipher 3x3',
        'module': hill,
        'key_label': 'Key 3x3 (9 angka, misal: 6,24,1,13,16,10,20,17,15)',
        'key_type': 'text',
        'key_hint': '9 angka dipisah koma',
    },
    'playfair': {
        'name': 'Playfair Cipher',
        'module': playfair,
        'key_label': 'Key (teks)',
        'key_type': 'text',
        'key_hint': 'A-Z',
    },
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        algo = request.form['algorithm']
        mode = request.form['mode']
        text = request.form['text']
        key = request.form['key']
        waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error = None
        output = ''
        steps = []
        extra = {}
        try:
            if algo == 'caesar':
                try:
                    k = int(key)
                except:
                    raise ValueError('Key harus berupa angka!')
                if mode == 'encrypt':
                    output, steps = caesar.caesar_encrypt(text, k)
                else:
                    output, steps = caesar.caesar_decrypt(text, k)
            elif algo == 'vigenere':
                if not key.isalpha():
                    raise ValueError('Key harus berupa huruf!')
                if mode == 'encrypt':
                    output, steps, key_full = vigenere.vigenere_encrypt(text, key)
                    extra['key_full'] = key_full
                else:
                    output, steps, key_full = vigenere.vigenere_decrypt(text, key)
                    extra['key_full'] = key_full
            elif algo == 'affine':
                try:
                    a, b = map(int, key.split(','))
                except:
                    raise ValueError('Key harus 2 angka dipisah koma!')
                if mode == 'encrypt':
                    output, steps = affine.affine_encrypt(text, a, b)
                else:
                    output, steps = affine.affine_decrypt(text, a, b)
                    if output is None:
                        raise ValueError('Key a tidak punya invers mod 26!')
            elif algo == 'hill2':
                try:
                    k = list(map(int, key.split(',')))
                    if len(k) != 4:
                        raise ValueError
                    key_matrix = np.array(k).reshape(2,2)
                except:
                    raise ValueError('Key harus 4 angka dipisah koma!')
                if mode == 'encrypt':
                    output, steps, padded = hill.hill_encrypt(text, key_matrix)
                    extra['padded'] = padded
                    extra['key_matrix'] = key_matrix
                else:
                    output, steps, padded = hill.hill_decrypt(text, key_matrix)
                    if output is None:
                        raise ValueError('Key tidak punya invers mod 26!')
                    extra['padded'] = padded
                    extra['key_matrix'] = key_matrix
            elif algo == 'hill3':
                try:
                    k = list(map(int, key.split(',')))
                    if len(k) != 9:
                        raise ValueError
                    key_matrix = np.array(k).reshape(3,3)
                except:
                    raise ValueError('Key harus 9 angka dipisah koma!')
                if mode == 'encrypt':
                    output, steps, padded = hill.hill_encrypt(text, key_matrix)
                    extra['padded'] = padded
                    extra['key_matrix'] = key_matrix
                else:
                    output, steps, padded = hill.hill_decrypt(text, key_matrix)
                    if output is None:
                        raise ValueError('Key tidak punya invers mod 26!')
                    extra['padded'] = padded
                    extra['key_matrix'] = key_matrix
            elif algo == 'playfair':
                if not key.isalpha():
                    raise ValueError('Key harus berupa huruf!')
                if mode == 'encrypt':
                    output, steps, table, pairs = playfair.playfair_encrypt(text, key)
                    extra['table'] = table
                    extra['pairs'] = pairs
                else:
                    output, steps, table, pairs = playfair.playfair_decrypt(text, key)
                    extra['table'] = table
                    extra['pairs'] = pairs
            else:
                raise ValueError('Algoritma tidak dikenali!')
            # Simpan history
            history = session.get('history', [])
            history.append({
                'algoritma': ALGORITHMS[algo]['name'],
                'mode': 'Enkripsi' if mode == 'encrypt' else 'Dekripsi',
                'input': text,
                'key': key,
                'output': output,
                'waktu': waktu
            })
            session['history'] = history[-20:]  # Simpan max 20
            session.modified = True
        except Exception as e:
            error = str(e)
        return render_template('index.html', algorithms=ALGORITHMS, selected=algo, mode=mode, text=text, key=key, output=output, steps=steps, error=error, extra=extra)
    return render_template('index.html', algorithms=ALGORITHMS)

@app.route('/history')
def history():
    history = session.get('history', [])
    return render_template('history.html', history=history)
    
if __name__ == '__main__':
    app.run(debug=True)
