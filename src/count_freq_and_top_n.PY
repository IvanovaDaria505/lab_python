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
