# Лаборторная работа 2
## Задание 1 — arrays.py
### min_max
```
def min_max(nums: list[float | int] ) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError
    return (min(nums), max(nums))
print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([1.5,2,2.0,-3.1]))
print(min_max([]))
```
<img width="1756" height="982" alt="arrays 1 1" src="https://github.com/user-attachments/assets/fcd9a06a-6ea0-47fd-aefd-706ee4d08020" />

### unique_sorted 
```
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

```
<img width="1434" height="604" alt="arrays 1 2" src="https://github.com/user-attachments/assets/ac271cbf-b6c9-4c8e-95b6-ea848aea417b" />

### flatten
```
def flatten(mat: list[list | tuple]) -> list:
    a=[]
    for i in mat:
        for m in i:
            if str(m) in '0123456789':
                a.append(m)
            else:
                raise TypeError
    return a 
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))   

```
<img width="1641" height="1107" alt="arrays1 3" src="https://github.com/user-attachments/assets/5daccf06-c020-4eb3-b8c2-453c4835e24e" />


## Задание 2 — matrix.py
### transpose
```
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []  
    f = len(mat[0])
    for r in mat:
        if len(r) != f:
            raise ValueError
    n= []
    for j in range(len(mat[0])):
        t = []
        for i in range(len(mat)):
            t.append(mat[i][j])
        n.append(t)
    return n
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

```
<img width="1446" height="1352" alt="matrix2 1" src="https://github.com/user-attachments/assets/28310327-0eba-4699-949f-823bb3cdef78" />

### row_sums
```
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []  
    f = len(mat[0])
    for r in mat:
        if len(r) != f:
            raise ValueError
    return [sum(row) for row in mat] 
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))     

```
<img width="1644" height="1029" alt="matrix2 2" src="https://github.com/user-attachments/assets/4d415b6a-5f65-497e-a84f-1482624e8209" />


### col_sums
```
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []  
    f = len(mat[0])
    for r in mat:
        if len(r) != f:
            raise ValueError
    w = []
    for j in range(len(mat[0])):
        col_sum = 0
        for i in range(len(mat)):
            col_sum += mat[i][j]
        w.append(col_sum)
    return w
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))

```
<img width="1491" height="1334" alt="matrix2 3" src="https://github.com/user-attachments/assets/398c2e6a-b8aa-486d-8268-b54df38962c7" />

## Задание 3 — tuples.py
```
from typing import Tuple

StudentRecord = Tuple[str, str, float]

def format_record(rec: StudentRecord) -> str:
    fio, group, gpa = rec
    fio_parts = [part.strip() for part in fio.split()]
    formatted_surname = fio_parts[0].capitalize()
    initials = ''.join([f'{name[0].upper()}.' for name in fio_parts[1:]])
    formatted_gpa = f'{gpa:.2f}'
    formatted_record = f"{formatted_surname} {initials}, гр. {group}, GPA {formatted_gpa}"
    return formatted_record

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.605)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
<img width="1817" height="1246" alt="tuples" src="https://github.com/user-attachments/assets/0c97cd51-cc2f-41b8-8b50-7f616fd00762" />





