import sys
import csv
from collections import Counter
from typing import Iterable, Sequence

sys.path.append(r"C:\VS\VS_MISIS\Misis\src\lab03")
from A import tokenize, normalize, count_freq, top_n
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        return normalize(p.read_text(encoding=encoding), True, True)
    except FileNotFoundError:
        print("Ошибка. Файл не найден.")
        return ""
    except UnicodeDecodeError:
        print("Неправильная кодировка.")
        return ""


def write_csv(rows, path, header=("word", "count")):
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            if len(r) == 2:
                w.writerow(r)
            else:
                return ValueError
    return ""


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(text)
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


print(
    write_csv(
        sorted_word_counts(
            frequencies_from_text(read_text("C:\VS\VS_MISIS\Misis\src\lab04\mua"))
        ),
        "C:\VS\VS_MISIS\Misis\src\lab04\\report.csv",
    )
)
