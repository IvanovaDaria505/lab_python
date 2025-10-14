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
        cu = c.get(w, 0)
        c[w] = cu + 1
    return c
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    t = []
    for w, count in freq.items():
        t.append((-count, w))
    t.sort()
    result = []
    for neg_count, w in t:
        result.append((w, -neg_count))
    return result[:n]
tok = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tok)
print(top_n(freq, n=2))
tok_2 = ["bb", "aa", "bb", "aa", "cc"]
freq_2 = count_freq(tok_2)
print(top_n(freq_2, n=2))
```
<img width="1291" height="1485" alt="2025-10-14_00-55-26" src="https://github.com/user-attachments/assets/c1b9e3fb-3948-4fae-9704-d8666c0d85bd" />


## Задание B — src/text_stats.py (скрипт со stdin)
```

```








