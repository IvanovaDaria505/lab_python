# Лаборторная работа 3
## Задание A — src/lib/text.py
### normalize
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text
print(normalize("ПрИвЕт\nМИр\t")) 
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
<img width="1341" height="814" alt="2025-10-14_00-24-25" src="https://github.com/user-attachments/assets/18db4d1f-9090-49f4-9406-42939b875468" />

### tokenize 
```
import re 
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

```
<img width="917" height="743" alt="2025-10-14_00-32-44" src="https://github.com/user-attachments/assets/3af0e37a-e1ac-4e92-8158-1e17534f9b4e" />


### count_freq + top_n
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    c = {}  
    for w in tokens:
        current_count = c.get(w, 0)
        c[w] = current_count + 1
    return c
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    temp_list = []
    for w, count in freq.items():
        temp_list.append((-count, w))
    temp_list.sort()
    result = []
    for neg_count, w in temp_list:
        result.append((w, -neg_count))

    return result[:n]
tokens_example = ["a", "b", "a", "c", "b", "a"]
freq_example = count_freq(tokens_example)
print(top_n(freq_example, n=2))
tokens_example_2 = ["bb", "aa", "bb", "aa", "cc"]
freq_example_2 = count_freq(tokens_example_2)
print(top_n(freq_example_2, n=2))
```
<img width="1071" height="1132" alt="2025-10-14_00-30-49" src="https://github.com/user-attachments/assets/7a18bdd9-d652-46eb-be5a-6feec4aa1e83" />

## Задание B — src/text_stats.py (скрипт со stdin)
```

```








