import re

def data_parsing(pages):
    task_data = []
    task_num = 0
    task = {}
    accumulating_code = False

    for page in pages:
        content = page["content"]

        match_task = re.search(r"TUGAS (\d+)", content)
        if match_task:
            if task: 
                task_data.append(task)

            task_num = int(match_task.group(1))
            task = {
                "tugas_num": task_num,
                "soal": "",
                "source_code": "",
                "penjelasan": "",
                "screenshot": "Screenshot placeholder",
            }
            accumulating_code = False

        match_soal = re.search(r"A\. Soal\n(.*?)\nB\. Source Code", content, re.DOTALL)
        if match_soal:
            task["soal"] = match_soal.group(1).strip()

        match_code_start = re.search(r"B\. Source Code\n(.*?)(?:\nC\.|$)", content, re.DOTALL)
        if match_code_start:
            task["source_code"] = match_code_start.group(1).strip()

        if accumulating_code:
            task["source_code"] += "\n" + content.strip()

        # Ambil penjelasan
        match_penjelasan = re.search(r"D\. Penjelasan\n(.*?)(?:$)", content, re.DOTALL)
        if match_penjelasan:
            task["penjelasan"] = match_penjelasan.group(1).strip()
            accumulating_code = False

    if task:
        task_data.append(task)

    return task_data
