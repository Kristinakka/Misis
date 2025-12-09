import argparse
import sys
from pathlib import Path

sys.path.append("C:\VS\VS_MISIS\Misis\src\lab04")
from io_txt_csv import *

sys.path.append("C:\VS\VS_MISIS\Misis\src\lab03")
from A import *


def cat(file_path, count=False):
    number = 1
    try:
        with open(file_path, encoding="utf-8") as f:
            for i in f:
                if count:
                    print(f"{number}. {i.strip()}")
                else:
                    print(i.strip())
                number += 1
    except FileNotFoundError:
        return f"Ошибка. файл {file_path} не найден!"


def stats(file_path, top=5):
    file_path = Path(file_path)
    try:
        txt = read_text(file_path)
        print(f"Всего слов: {len(tokenize(txt))}")
        print(f"Уникальных слов: {len(set(tokenize(txt)))}")
        print("Top-5:")
        for i in top_n(count_freq(tokenize(txt)), top):
            print(f"{i[0]}:{i[1]}")
    except FileNotFoundError:
        return f"Ошибка. файл {file_path} не найден!"


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument(
        "-n", dest="count", action="store_true", help="Нумеровать строки"
    )

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    if args.command == "cat":
        cat(args.input, args.count)

    elif args.command == "stats":
        stats(args.input, args.top)


if __name__ == "__main__":
    main()

# python3 C:\VS\VS_MISIS\Misis\src\lab06\cli_text.py stats --input C:\VS\VS_MISIS\Misis\data\lab06\in\txt --top 5
# python3 python3 C:\VS\VS_MISIS\Misis\src\lab06\cli_text.py cat --input C:\VS\VS_MISIS\Misis\data\lab06\in\txt -n
