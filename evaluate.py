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
        evaluation = re.sub(r"[\*#]", "", evaluation).lower()
        print("Hasil Evaluasi Struktur Laporan:")
        print(evaluation)

        match_kesimpulan = re.search(r"kesimpulan:\s*(.*?)\n", evaluation)
        kesimpulan = match_kesimpulan.group(1).strip() if match_kesimpulan else None

        match_nilai_akhir = re.search(r"nilai akhir:\s*(.*?)(?:$)", evaluation)
        nilai_akhir = match_nilai_akhir.group(1).strip() if match_nilai_akhir else None

        # Output hasil
        # print("Kesimpulan:", kesimpulan)
        # print("Nilai Akhir:", nilai_akhir)

        return kesimpulan, nilai_akhir

    except Exception as e:
        print("Terjadi kesalahan:", e)
        return "", ""


def eval_answer(data, promt):
    messages = [    
        {"role": "system", "content": "Kamu adalah seorang dosen dengan pengalaman lebih dari 5 tahun yang bertugas mengevaluasi source code dan penjelasan dari setiap soal."},
        {"role": "user", "content": f"Evaluasi laporan berikut:\n\n{data}\n\n{promt}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.5
        )
        
        evaluation = response['choices'][0]['message']['content']
        evaluation = re.sub(r"[\*#]", "", evaluation).lower()
        print("Hasil Evaluasi Laporan:")
        print(evaluation)

        match_saran = re.search(r"saran:\s*(.*?)\n", evaluation, re.DOTALL)
        saran = match_saran.group(1).strip() if match_saran else None

        match_nilai = re.search(r"nilai akhir:\s*(\d+)", evaluation)
        nilai_akhir = match_nilai.group(1).strip() if match_nilai else None

        return saran, nilai_akhir
    
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return "", ""