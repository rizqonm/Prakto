import re

# Teks yang diberikan
text = """
Hasil Evaluasi Laporan:
### Evaluasi Laporan

#### Tugas 1:
1. **Source Code:** Source code tidak lengkap dan terdapat kesalahan sintaks. Perlu dilakukan perbaikan pada penulisan kode agar sesuai dengan soal.

2. **Penjelasan:** Penjelasan cukup jelas dalam menjelaskan cara program bekerja dan alur pemecahan masalah.

#### Tugas 2:
1. **Source Code:** Source code sesuai dengan soal dan telah mengimplementasikan pendekatan object-oriented dengan baik.

2. **Penjelasan:** Penjelasan sudah menjelaskan dengan baik bagaimana program bekerja dan fitur-fitur yang dimiliki.    

#### Tugas 3:
1. **Source Code:** Source code sesuai dengan soal dan telah menggunakan fitur functional programming dengan baik.      

2. **Penjelasan:** Penjelasan cukup lengkap dan menjelaskan penggunaan fitur functional programming dengan baik.        

### Kesimpulan:
- Source code Tugas 1 perlu perbaikan, sementara Tugas 2 dan Tugas 3 sudah sesuai.
- Penjelasan pada semua tugas cukup jelas dan informatif.

### Saran: Perbaiki source code pada Tugas 1 agar sesuai dengan soal dan perhatikan sintaks yang digunakan.

### Nilai akhir: 85
"""

text = re.sub(r"[\*#]", "", text).lower()
# print(text)
# Menemukan saran
match_saran = re.search(r"saran:\s*(.*?)\n", text, re.DOTALL)
saran = match_saran.group(1).strip() if match_saran else None

# Menemukan nilai akhir
match_nilai = re.search(r"nilai akhir:\s*(\d+)", text)
nilai_akhir = match_nilai.group(1).strip() if match_nilai else None

# Menampilkan hasil
print(f"Saran: {saran}")
print(f"Nilai Akhir: {nilai_akhir}")
