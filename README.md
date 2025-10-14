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
from lib.text import normalize, tokenize, count_freq, top_n
import sys
def main():
    text = sys.stdin.buffer.read().decode('utf-8')
    if not text.strip():
        print("Нет входных данных")
        return
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    

    if not tokens:
        print("В тексте не найдено слов")
        return

    total_words = len(tokens)
    freq_dict = count_freq(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":  
    main()
```
<img width="1522" height="1255" alt="2025-10-14_13-02-55" src="https://github.com/user-attachments/assets/49ca2b2a-d0f1-4a2c-a504-6bb0b6de3c1f" />
<img width="1682" height="195" alt="2025-10-14_13-03-50" src="https://github.com/user-attachments/assets/f7554834-5274-4034-8289-27f0cfc1e782" />










