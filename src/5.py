import sys
import re

def normalize(text: str) -> str:
    return text.casefold()

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]

def main():
    text = sys.stdin.read()

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
    echo 'Привет, мир! Привет!!!' | python3 src/lab3/text_stats.py
    