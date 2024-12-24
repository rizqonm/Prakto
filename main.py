import os
import json
from extract import extract_pdf
from preprocess import data_parsing
from evaluate_structure import eval_structure

input_path = "laprak/ori"
struct_path = "promt_structure.txt"

for file_name in os.listdir(input_path):
    pdf_path = os.path.join(input_path, file_name)
    epdf = extract_pdf(pdf_path)

    tasks = data_parsing(epdf)
    data = json.dumps(tasks, indent=4, ensure_ascii=False)
    # print(data)

    with open(struct_path, "r", encoding="utf-8") as file:
        promt_struct = file.read()

    eval_structure(data, promt_struct)
    # kesimpulan_s, nilai_s = eval_structure(data, promt_struct)
    # print("Kesimpulan:", kesimpulan_s)
    # print("Nilai Akhir:", nilai_s)