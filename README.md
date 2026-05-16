# Simulasi Kriptografi Klasik

Aplikasi web edukatif untuk mensimulasikan algoritma kriptografi klasik dengan visualisasi proses perhitungan secara detail.

## Fitur

## Teknologi

## Instalasi
1. Clone repo ini
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:
   ```bash
   python app.py
   ```

## Deploy ke Vercel
1. Push project ini ke GitHub.
2. Import repository ke Vercel.
3. Pastikan framework terdeteksi sebagai Python.
4. Vercel akan memakai [app.py](app.py) sebagai entrypoint Flask.
5. Jika perlu, biarkan `vercel.json` yang ada di root project tetap dipakai.
6. Tambahkan environment variable `SECRET_KEY` di Vercel untuk session yang lebih aman.

Catatan: history disimpan di session cookie, jadi data history bersifat sementara dan mengikuti browser yang dipakai.

- /static

## Demo
https://kriptografi-hilminurpadilah.my.id/

