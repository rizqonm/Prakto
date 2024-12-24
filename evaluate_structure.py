import openai
from dotenv import load_dotenv
import os

# Memuat API Key dari file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

# Data laporan
data = [
    {
        "tugas_num": 1,
        "soal": "Buatlah program interaktif untuk menyelesaikan permasalahan menara Hanoi",
        "source_code": "hanoi.kt\n...",
        "penjelasan": "Program ini memungkinkan pengguna untuk memasukkan jumlah\ncakram...",
        "screenshot": "Screenshot placeholder"
    },
    {
        "tugas_num": 2,
        "soal": "Client meminta program pendataan buku. Dengan fitur menambahkan buku\ndan melihat seluruh daftar buku yang ada...",
        "source_code": "dataBuku.kt\n...",
        "penjelasan": "Program ini mengikuti paradigma object-oriented dengan dua kelas\nutama...",
        "screenshot": "Screenshot placeholder"
    }
]

# Mengirim data ke OpenAI untuk evaluasi
messages = [
    {"role": "system", "content": "Kamu adalah asisten AI yang bertugas mengevaluasi struktur laporan."},
    {"role": "user", "content": f"Evaluasi struktur laporan berikut:\n{data}\n\n1. Apakah terdapat TUGAS 1, jika iya, apakah didalamnya terdapat soal, source code, screenshot, penjelasan?\n2. Apakah terdapat TUGAS 2, jika iya, apakah didalamnya terdapat soal, source code, screenshot, penjelasan?\n\nBeri hasil evaluasi akhir dalam format berikut:\n- Kesimpulan singkat apakah semua elemen tersedia.\n- Nilai akhir dengan format x/100 berdasarkan kelengkapan elemen struktur laporan."}
]

try:
    # Mengirim permintaan ke OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.5
    )
    
    evaluation = response['choices'][0]['message']['content']
    print("Hasil Evaluasi Struktur Laporan:")
    print(evaluation)
except Exception as e:
    print("Terjadi kesalahan:", e)
