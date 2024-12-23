import re
import json

# Input data
pages = [
    {
        "page": 1,
        "content": "LABORATORIUM PEMBELAJARAN ILMU KOMPUTER\nFAKULTAS ILMU KOMPUTER\nUNIVERSITAS BRAWIJAYA\nBAB : PEMROGRAMAN KOTLIN\nNAMA : MUHAMMAD RIZQON MAULANA\nNIM : 215150201111022\nTANGGAL : 11/09/2023\nASISTEN : - ANAK AGUNG GDE AGASTYA MAHESWARA\n- GEDE PRAMANANDA KUSUMA WISESA\nTUGAS 1\nA. Soal\nBuatlah program interaktif untuk menyelesaikan permasalahan menara Hanoi\nB. Source Code\nhanoi.kt\n1 package bab2\n2\n3 import java.util.Scanner\n4\nfun towerOfHanoi(n: Int, source: Char, auxiliary:\n5\nChar, destination: Char) {\n6\nif (n == 1) {\n7\nprintln(\"Memindahkan cakram 1 dari $source\n8\nke $destination\")\n9 return\n10 }\n11 towerOfHanoi(n - 1, source, destination,\n12 auxiliary)\n13 println(\"Memindahkan cakram $n dari $source ke\n$destination\")\n14\ntowerOfHanoi(n - 1, auxiliary, source,\n15\ndestination)\n16\n}\n17\n18\nfun main() {\n19 val scanner = Scanner(System.`in`)\n20 println(\"============================\")\n21 println(\" TOWER OF HANOI \")\n22 println(\"============================\")\n23 print(\"Masukkan jumlah cakram : \")\nval n = scanner.nextInt()\n24\n25\nif(n < 1) {\n26\nprintln(\"Jumlah cakram yang anda masukkan\n27\ntidak valid\")\n28\n} else {\n29 println(\"Cara menyelesaikan Tower of Hanoi\n30 dengan $n cakram adalah\")\n31 towerOfHanoi(n, 'A', 'B', 'C')\n32 }\n33 }"
    },
    {
        "page": 2,
        "content": "C. Screenshot\nD. Penjelasan\nProgram ini memungkinkan pengguna untuk memasukkan jumlah\ncakram yang ingin dipindahkan dalam permainan Tower of Hanoi. Setelah\ninput diterima, program akan mencetak langkah-langkah yang diperlukan\nuntuk menyelesaikan masalah tersebut. Program menggunakan rekursif untuk\nmemecahkan masalah ini. Jika jumlah cakram adalah 1, program langsung\nmencetak langkah pemindahan cakram. Jika tidak, program memecahkan\nmasalah menjadi tiga langkah: pertama, memindahkan n-1 cakram dari tiang\nawal ke tiang bantu dengan menggunakan tiang tujuan sebagai tiang bantu;\nkedua, memindahkan cakram ke-n dari tiang awal ke tiang tujuan; dan ketiga,\nmemindahkan kembali n-1 cakram dari tiang bantu ke tiang tujuan dengan\nmenggunakan tiang awal sebagai tiang bantu. Setiap langkah pemindahan\ncakram dicetak ke layar sehingga pengguna dapat melihat cara menyelesaikan\nmasalah Tower of Hanoi dengan jumlah cakram yang dimasukkan."
    },
    {
        "page": 3,
        "content": "TUGAS 2\nA. Soal\nClient meminta program pendataan buku. Dengan fitur menambahkan buku\ndan melihat seluruh daftar buku yang ada. Selesaikan program tersebut dengan\npendekatan object oriented dan interaktif\nB. Source Code\ndataBuku.kt\n1 package bab2\n2\n3 class Buku(val judul: String, val pengarang:\n4 String) {\n5 override fun toString(): String {\n6 return \"Judul: $judul, Pengarang:\n7 $pengarang\"\n8 }\n9 }\n10\n11 class Perpustakaan {\n12 private val daftarBuku =\n13 mutableListOf<Buku>()\n14\n15 fun tambahBuku(buku: Buku) {\n16 daftarBuku.add(buku)\n17 println(\"Buku berhasil ditambahkan ke\n18 daftar buku.\")\n19 }\n20\n21 fun lihatDaftarBuku() {\n22 if (daftarBuku.isEmpty()) {\n23 println(\"daftar buku kosong.\")\n24 } else {\n25 println(\"Daftar Buku:\")\n26 for ((index, buku) in\n27 daftarBuku.withIndex()) {\n28 println(\"${index + 1}. $buku\")\n29 }\n30 }\n31 }\n32 }\n33\n34 fun main() {\n35\n36 println(\"===================================\")\n37 println(\" SISTEM PENDATAAN BUKU\n38 \")\n39\n40 println(\"===================================\")\n41\n42 val perpustakaan = Perpustakaan()"
    },
    {
        "page": 4,
        "content": "43\n44 while (true) {\n45 println(\"\\nMenu:\")\n46 println(\"1. Tambah Buku\")\n47 println(\"2. Lihat Daftar Buku\")\n48 println(\"3. Keluar\")\n49 print(\"Pilih tindakan : \")\n50\n51 when (readLine()?.toIntOrNull()) {\n52 1 -> {\n53 print(\"Masukkan judul buku: \")\n54 val judul = readLine()\n55 print(\"Masukkan nama\n56 pengarang: \")\n57 val pengarang = readLine()\n58 if (judul != null &&\n59 pengarang != null) {\n60 val buku = Buku(judul,\n61 pengarang)\n62\n63 perpustakaan.tambahBuku(buku)\n64 } else {\n65 println(\"Input tidak\n66 valid.\")\n67 }\n68 }\n69 2 ->\n70 perpustakaan.lihatDaftarBuku()\n71 3 -> {\n72 println(\"Terima kasih telah\n73 menggunakan program pendataan buku.\")\n74 return\n75 }\n76 else -> println(\"Pilihan tidak\n77 valid. Silakan pilih lagi.\")\n78 }\n79 }\n80 }\nC. Screenshot"
    },
    {
        "page": 5,
        "content": "D. Penjelasan\nProgram ini mengikuti paradigma object-oriented dengan dua kelas\nutama, yaitu Buku dan Perpustakaan. Kelas Buku digunakan untuk\nmerepresentasikan informasi buku, sedangkan kelas Perpustakaan\nbertanggung jawab untuk mengelola daftar buku yang mana terdapat 2 fungsi\nutama yaitu tambahBuku dan lihatDaftarBuku. Program ini interaktif dengan\nmenggunakan looping, memungkinkan pengguna untuk menambahkan buku\nbaru atau melihat daftar buku yang ada secara terus-menerus sampai pengguna\nkeluar dari program. Selama interaksi, program juga memberikan pesan-pesan\nyang informatif. Ini memanfaatkan fitur-fitur Kotlin seperti classes, functions,\ndan control flow untuk memberikan pengalaman yang sederhana namun\nefektif dalam mengelola daftar buku."
    }
]

# Function to extract tasks
def extract_tasks(pages):
    task_data = []
    task_num = 0
    task = {}

    for page in pages:
        content = page["content"]

        # Check if a new task starts
        match_task = re.search(r"TUGAS (\d+)", content)
        if match_task:
            if task:
                task_data.append(task)  # Save the previous task

            task_num = int(match_task.group(1))
            task = {"tugas_num": task_num, "soal": "", "source_code": "", "penjelasan": "", "screenshot": "Screenshot placeholder"}

        # Extract Soal
        match_soal = re.search(r"A\. Soal\n(.*?)\nB\. Source Code", content, re.DOTALL)
        if match_soal:
            task["soal"] = match_soal.group(1).strip()

        # Extract Source Code
        match_code = re.search(r"B\. Source Code\n(.*?)\n(?:C\. Screenshot|D\. Penjelasan)", content, re.DOTALL)
        if match_code:
            task["source_code"] += match_code.group(1).strip()

        # Extract Penjelasan
        match_penjelasan = re.search(r"D\. Penjelasan\n(.*?)$", content, re.DOTALL)
        if match_penjelasan:
            task["penjelasan"] = match_penjelasan.group(1).strip()

    if task:
        task_data.append(task)  # Save the last task

    return task_data

# Process the data
tasks = extract_tasks(pages)

# Output the result as JSON
output = json.dumps(tasks, indent=4, ensure_ascii=False)
print(output)
