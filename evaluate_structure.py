import openai
from dotenv import load_dotenv
import os
import re

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def eval_structure(data, promt):
    messages = [
        {"role": "system", "content": "Kamu adalah asisten AI yang bertugas mengevaluasi struktur laporan."},
        {"role": "user", "content": f"Evaluasi struktur laporan berikut:\n{data}\n\n{promt}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300,
            temperature=0.5
        )
        
        evaluation = response['choices'][0]['message']['content']
        print("Hasil Evaluasi Struktur Laporan:")
        print(evaluation)
        evaluation = evaluation.lower()

        # Regex untuk mengambil bagian Kesimpulan
        match_kesimpulan = re.search(r"kesimpulan:\s*(.*?)\n", evaluation)
        kesimpulan = match_kesimpulan.group(1).strip() if match_kesimpulan else None

        # Regex untuk mengambil bagian Nilai Akhir
        match_nilai_akhir = re.search(r"nilai akhir:\s*(.*?)", evaluation)
        nilai_akhir = match_nilai_akhir.group(1).strip() if match_nilai_akhir else None

        # Output hasil
        print("Kesimpulan:", kesimpulan)
        print("Nilai Akhir:", nilai_akhir)

    except Exception as e:
        print("Terjadi kesalahan:", e)


def eval_answer(data, promt):
    messages = [    
        {"role": "system", "content": "Kamu adalah asisten AI yang bertugas mengevaluasi source code dan penjelasan dari setiap soal."},
        {"role": "user", "content": f"Evaluasi laporan berikut:\n\n{data}\n\nUntuk setiap tugas, lakukan:\n1. Periksa apakah source code sesuai dengan soal.\n2. Periksa apakah penjelasan menjelaskan dengan jelas bagaimana program berjalan.\n\nHasil evaluasi harus mencakup:\n- Kesimpulan untuk setiap tugas, apakah source code dan penjelasan sudah sesuai.\n- Kesimpulan keseluruhan apakah semua elemen sudah sesuai.\n- Nilai akhir dengan format x/100.\n- Saran perbaikan jika ada yang salah."}
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
        print("Hasil Evaluasi Laporan:")
        print(evaluation)
    except Exception as e:
        print("Terjadi kesalahan:", e)