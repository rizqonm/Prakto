import json

# Data JSON awal (simulasikan dengan copy dari JSON Anda)
data_json = [
    {
        "page": 1,
        "content": "LABORATORIUM PEMBELAJARAN ILMU KOMPUTER\nFAKULTAS ILMU KOMPUTER\nUNIVERSITAS BRAWIJAYA\nBAB : PEMROGRAMAN KOTLIN\nNAMA : MUHAMMAD RIZQON MAULANA\nNIM : 215150201111022\nTANGGAL : 11/09/2023\nASISTEN : - ANAK AGUNG GDE AGASTYA MAHESWARA\n- GEDE PRAMANANDA KUSUMA WISESA\nTUGAS 1\nA. Soal\nBuatlah program interaktif untuk menyelesaikan permasalahan menara Hanoi\nB. Source Code\nhanoi.kt\n1 package bab2\n2\n3 import java.util.Scanner\n4\nfun towerOfHanoi(n: Int, source: Char, auxiliary:\n5\nChar, destination: Char) {\n6\nif (n == 1) {\n7\nprintln(\"Memindahkan cakram 1 dari $source\n8\nke $destination\")\n9 return\n10 }\n11 towerOfHanoi(n - 1, source, destination,\n12 auxiliary)\n13 println(\"Memindahkan cakram $n dari $source ke\n$destination\")\n14\ntowerOfHanoi(n - 1, auxiliary, source,\n15\ndestination)\n16\n}\n17\n18\nfun main() {\n19 val scanner = Scanner(System.`in`)\n20 println(\"============================\")\n21 println(\" TOWER OF HANOI \")\n22 println(\"============================\")\n23 print(\"Masukkan jumlah cakram : \")\nval n = scanner.nextInt()\n24\n25\nif(n < 1) {\n26\nprintln(\"Jumlah cakram yang anda masukkan\n27\ntidak valid\")\n28\n} else {\n29 println(\"Cara menyelesaikan Tower of Hanoi\n30 dengan $n cakram adalah\")\n31 towerOfHanoi(n, 'A', 'B', 'C')\n32 }\n33 }"
    },
    {
        "page": 2,
        "content": "C. Screenshot\nD. Penjelasan\nProgram ini memungkinkan pengguna untuk memasukkan jumlah\ncakram yang ingin dipindahkan dalam permainan Tower of Hanoi. Setelah\ninput diterima, program akan mencetak langkah-langkah yang diperlukan\nuntuk menyelesaikan masalah tersebut. Program menggunakan rekursif untuk\nmemecahkan masalah ini. Jika jumlah cakram adalah 1, program langsung\nmencetak langkah pemindahan cakram. Jika tidak, program memecahkan\nmasalah menjadi tiga langkah: pertama, memindahkan n-1 cakram dari tiang\nawal ke tiang bantu dengan menggunakan tiang tujuan sebagai tiang bantu;\nkedua, memindahkan cakram ke-n dari tiang awal ke tiang tujuan; dan ketiga,\nmemindahkan kembali n-1 cakram dari tiang bantu ke tiang tujuan dengan\nmenggunakan tiang awal sebagai tiang bantu. Setiap langkah pemindahan\ncakram dicetak ke layar sehingga pengguna dapat melihat cara menyelesaikan\nmasalah Tower of Hanoi dengan jumlah cakram yang dimasukkan."
    }
]

# Fungsi untuk memproses data JSON menjadi struktur yang diinginkan
def preprocess_tugas(data):
    tugas_data = []
    current_tugas = {}

    for page in data:
        content = page['content']

        # Pisahkan berdasarkan line break
        lines = content.splitlines()

        for line in lines:
            # Deteksi tugas baru
            if line.startswith("TUGAS"):
                if current_tugas:
                    tugas_data.append(current_tugas)
                current_tugas = {
                    "tugas_num": int(line.split()[1]),
                    "soal": "",
                    "source_code": "",
                    "penjelasan": "",
                    "screenshot": ""
                }

            # Deteksi bagian soal
            elif line.startswith("A. Soal"):
                current_tugas["soal"] = line.split("A. Soal")[-1].strip()

            # Deteksi bagian source code
            elif line.startswith("B. Source Code"):
                current_tugas["source_code"] += line.split("B. Source Code")[-1].strip()

            # Deteksi bagian screenshot
            elif line.startswith("C. Screenshot"):
                current_tugas["screenshot"] += "Screenshot placeholder"

            # Deteksi bagian penjelasan
            elif line.startswith("D. Penjelasan"):
                current_tugas["penjelasan"] += line.split("D. Penjelasan")[-1].strip()

    # Tambahkan tugas terakhir jika ada
    if current_tugas:
        tugas_data.append(current_tugas)

    return tugas_data

# Proses data JSON
tugas_data = preprocess_tugas(data_json)

# Cetak hasil
print(json.dumps(tugas_data, indent=2))
