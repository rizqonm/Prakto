import pdfplumber
import json
import os

pdf_path = "tes_laprak2.pdf"
base_name = os.path.splitext(os.path.basename(pdf_path))[0]
output_path = f"e_{base_name}.json"
output = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        text = page.extract_text()
        output.append({
            "page": page_num + 1,
            "content": text.strip() if text else ""
        })

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)

print(f"Hasil ekstraksi disimpan dalam file: {output_path}")