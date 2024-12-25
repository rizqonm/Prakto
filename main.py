import os
import json
import csv
from extract import extract_pdf
from preprocess import data_parsing
from evaluate import eval_structure, eval_answer

input_path = "laprak/ori"
struct_path = "promt_structure.txt"
ans_path = "promt_answer.txt"
output_path = "evaluation_results.csv"

results = []

for file_name in os.listdir(input_path):
    pdf_path = os.path.join(input_path, file_name)
    epdf = extract_pdf(pdf_path)

    tasks = data_parsing(epdf)
    data = json.dumps(tasks, indent=4, ensure_ascii=False)

    with open(struct_path, "r", encoding="utf-8") as file:
        promt_struct = file.read()
    with open(ans_path, "r", encoding="utf-8") as file:
        promt_ans = file.read()

    kesimpulan_s, nilai_s = eval_structure(data, promt_struct)
    kesimpulan_a, nilai_a = eval_answer(data, promt_ans)

    results.append([file_name, kesimpulan_s, nilai_s, kesimpulan_a, nilai_a])

with open(output_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Nama", "Kesimpulan Struktur", "Nilai Struktur", "Saran", "Nilai Jawaban"])
    writer.writerows(results)

print(f"Data berhasil disimpan ke {output_path}")