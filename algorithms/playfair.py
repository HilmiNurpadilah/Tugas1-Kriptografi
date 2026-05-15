"""
Modul Playfair Cipher
"""
def generate_table(key):
    key = ''.join([c.upper() for c in key if c.isalpha()])
    table = []
    used = set()
    for c in key:
        if c not in used and c != 'J':
            table.append(c)
            used.add(c)
    for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if c not in used:
            table.append(c)
            used.add(c)
    return [table[i*5:(i+1)*5] for i in range(5)]

def find_position(table, char):
    for i, row in enumerate(table):
        for j, c in enumerate(row):
            if c == char or (char == 'J' and c == 'I'):
                return i, j
    return None, None

def prepare_text(text, for_encrypt=True):
    text = ''.join([c.upper() for c in text if c.isalpha()])
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def playfair_encrypt(text, key):
    steps = []
    table = generate_table(key)
    pairs = prepare_text(text)
    result = ''
    steps.append(f"Tabel 5x5 dari key: {table}")
    for a, b in pairs:
        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)
        if r1 == r2:
            enc_a = table[r1][(c1+1)%5]
            enc_b = table[r2][(c2+1)%5]
            rule = "Baris sama, geser kanan"
        elif c1 == c2:
            enc_a = table[(r1+1)%5][c1]
            enc_b = table[(r2+1)%5][c2]
            rule = "Kolom sama, geser bawah"
        else:
            enc_a = table[r1][c2]
            enc_b = table[r2][c1]
            rule = "Bentuk persegi, tukar kolom"
        steps.append(f"{a}{b}: {rule} → {enc_a}{enc_b}")
        result += enc_a + enc_b
    return result, steps, table, pairs

def playfair_decrypt(text, key):
    steps = []
    table = generate_table(key)
    pairs = prepare_text(text, for_encrypt=False)
    result = ''
    steps.append(f"Tabel 5x5 dari key: {table}")
    for a, b in pairs:
        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)
        if r1 == r2:
            dec_a = table[r1][(c1-1)%5]
            dec_b = table[r2][(c2-1)%5]
            rule = "Baris sama, geser kiri"
        elif c1 == c2:
            dec_a = table[(r1-1)%5][c1]
            dec_b = table[(r2-1)%5][c2]
            rule = "Kolom sama, geser atas"
        else:
            dec_a = table[r1][c2]
            dec_b = table[r2][c1]
            rule = "Bentuk persegi, tukar kolom"
        steps.append(f"{a}{b}: {rule} → {dec_a}{dec_b}")
        result += dec_a + dec_b
    return result, steps, table, pairs
