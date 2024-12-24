import openai
from dotenv import load_dotenv
import os
import re

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def eval_struct(output):
    messages = [
        {"role": "system", "content": "Kamu adalah asisten AI yang bertugas mengevaluasi source code dan penjelasan dari setiap soal."},
        {"role": "user", "content": f"Evaluasi laporan berikut:\n\n{output}\n\nUntuk setiap tugas, lakukan:\n1. Periksa apakah source code sesuai dengan soal.\n2. Periksa apakah penjelasan menjelaskan dengan jelas bagaimana program berjalan.\n\nHasil evaluasi harus mencakup:\n- Kesimpulan untuk setiap tugas, apakah source code dan penjelasan sudah sesuai.\n- Kesimpulan keseluruhan apakah semua elemen sudah sesuai.\n- Nilai akhir dengan format x/100.\n- Saran perbaikan jika ada yang salah."}
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

        match_kesimpulan = re.search(r"\*\*Kesimpulan:\*\*\s*(.*)", evaluation)
        kesimpulan = match_kesimpulan.group(1).strip() if match_kesimpulan else None
        match_nilai = re.search(r"\*\*Nilai Akhir:\*\*\s*(\d+/?\d*)", evaluation)
        nilai = match_nilai.group(1).strip() if match_nilai else None

    except Exception as e:
        print("Terjadi kesalahan:", e)

    return kesimpulan, nilai