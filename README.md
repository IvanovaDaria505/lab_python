## Лабораторная работа 5
### Задание A — JSON ↔ CSV
```python
import csv, json, sys, os
from pathlib import Path
def is_valid_json_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
        
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return isinstance(json_data, list) and len(json_data) > 0 and all(isinstance(item, dict) for item in json_data) 
    except:
        return False

def is_valid_csv_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
            
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  
            header = next(reader, None) 
            return header is not None and len(header) > 0
    except:
        return False

def json_to_csv(json_path: str, csv_path: str) -> None:
    if not is_valid_json_file(json_path): 
        print("ValueError: Input file is not a valid JSON or is empty")
        sys.exit(1) 
    json_path=Path(json_path)
    csv_path=Path(csv_path)
    if json_path.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")
    

    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file) 

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys()) 
        writer.writeheader()  
        writer.writerows(json_data) 

def csv_to_json(csv_path: str, json_path: str) -> None:
    if not is_valid_csv_file(csv_path):
        print("ValueError: Input file is not a valid CSV or is empty")
        sys.exit(1)
    json_path=Path(json_path)
    csv_path=Path(csv_path)
    if json_path.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат выходного файла: ожидается .json")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  
        data = list(reader) 
    
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4) 
csv_to_json(r"C:\Users\Home\lab_python\lab_python-2\data\samples\people.csv",r"C:\Users\Home\lab_python\lab_python-2\data\out\people_from_csv.json")

json_to_csv( r"C:\Users\Home\lab_python\lab_python-2\data\samples\people.json",  r"C:\Users\Home\lab_python\lab_python-2\data\out\people_from_json.csv" )
```

![Картинка 1](./images/image02.png)
![Картинка 1](./images/image03.png)
![Картинка 1](./images/image04.png)

### Задание B — CSV → XLSX

```python
import os
import csv
import sys
from pathlib import Path
from openpyxl import Workbook 

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None: 
    if not os.path.exists(csv_path):  
        print("FileNotFoundError") 
        sys.exit(1) 
    xlsx_path=Path(xlsx_path)
    csv_path=Path(csv_path)
    if xlsx_path.suffix.lower() != ".xlsx":
        raise ValueError(f"Неверный формат выходного файла: ожидается .xlsx")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")

    if os.path.getsize(csv_path) == 0: 
        print("ValueError")
        sys.exit(1)
    wb = Workbook() 
    ws = wb.active  
    ws.title = "Sheet1" 

    with open(csv_path, "r", encoding="utf-8") as csv_file: 
        reader = csv.reader(csv_file) 
        for row in reader: 
            ws.append(row) 
    for column_cells in ws.columns: 
        max_length = 0 
        column_letter = column_cells[0].column_letter 
        for cell in column_cells: 
            if cell.value: 
                max_length = max(max_length, len(str(cell.value))) 
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8) #обращается к настройкам ширины конкретной колонки, устанавливает ширину колонки, максимальная длина + 2 символа для отступа, 8- выбирает большее значение между расчитанной шириной и минимальной шириной 8 
    wb.save(xlsx_path)
csv_to_xlsx(r"C:\Users\Home\lab_python\lab_python-2\data\samples\cities.csv", r"C:\Users\Home\lab_python\lab_python-2\data\out\people.xlsx")    
```
![Картинка 1](./images/image05.png)
![Картинка 1](./images/image06.png)