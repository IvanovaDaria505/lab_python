from io_txt_csv import read_text, write_csv, ensure_parent_dir
import sys
from pathlib import Path
import os

sys.path.append(r'C:\Users\Home\Documents\GitHub\lab_01\lib')

from text import normalize, tokenize, count_freq, top_n


def exist_path(path_f: str):
    return os.path.exists(path_f)


def main(file: str, encoding: str = 'utf-8'):
    if not exist_path(file):
        return FileExistsError
    text = read_text(file, encoding=encoding)
    norm = normalize(text)
    tokens = tokenize(norm)
    top = top_n(count_freq(tokens), 5)
    top_sort = sorted(top, key=lambda x: (x[1], x[0]), reverse=True)
    write_csv(top_sort, os.path.dirname(file) + r'\report.csv' , header=('word','count'))
    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(count_freq(tokens))}')
    print('Топ-5:')
    for cursor in top_sort:
        print(f'{cursor[0]}: {cursor[-1]}')
main(r'C:\Users\Home\Documents\GitHub\lab_01\data\input.txt')