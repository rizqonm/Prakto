import re

text = '1. Ya, terdapat TUGAS 1. Didalamnya terdapat soal, source code, dan penjelasan.\n2. Ya, terdapat TUGAS 2. Didalamnya terdapat soal, source code, dan penjelasan.\n3. Ya, terdapat TUGAS 3. Didalamnya terdapat soal, source code, dan penjelasan.\n\n- Kesimpulan: Semua elemen yang diperlukan (soal, source code, penjelasan) tersedia untuk setiap tugas.\n- Nilai akhir: 100'

# Regex untuk mengambil bagian Kesimpulan
match_kesimpulan = re.search(r"Kesimpulan:\s*(.*?)\n", text)
kesimpulan = match_kesimpulan.group(1).strip() if match_kesimpulan else None

# Regex untuk mengambil bagian Nilai Akhir
match_nilai_akhir = re.search(r"Nilai akhir:\s*(\d+)", text)
nilai_akhir = match_nilai_akhir.group(1).strip() if match_nilai_akhir else None

# Output hasil
print("Kesimpulan:", kesimpulan)
print("Nilai Akhir:", nilai_akhir)
