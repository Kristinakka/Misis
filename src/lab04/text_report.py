import argparse
import os
from io_txt_csv import *

# python3 src/lab04/text_report.py --in data/in.txt --out data/out.csv


def main():
    parser = argparse.ArgumentParser(
        description="Обработка файлов"
    )  # Переменная, позволяющая обработать код запуска на входе
    parser.add_argument(
        "--in", dest="input_file", required=True
    )  # Добавляем в обработку аргумент --in, ответственный за ввод текста
    parser.add_argument(
        "--out", dest="output_file", required=True
    )  # Добавляем в обработку аргумент --out, ответственный за вывод csv

    args = parser.parse_args()  # Разбиваем код запуска на аргументы in и out

    # Работа с файлами
    process_files(args.input_file, args.output_file)


def process_files(input_path, output_path):
    # Создаем папку для выходного файла, если её нет
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:  # Пытаемся присвоить переменной all_text прочитанный текст из пути в аргументе in
        all_text = read_text(input_path, encoding="utf-8")

        data = []
        for i in top_n(
            count_freq(tokenize(all_text)), 5
        ):  # Перебираем весь текст через функции для нормализации, токенизации и подсчёта частоты слов
            data.append(((f"{i[0]}"), (f"{i[1]}")))  # Добавляем 1 и 2 значиния в папку

        write_csv(
            data, output_path, ("word", "count")
        )  # Используем функцию для написания csv

    except FileNotFoundError:
        print(f"Файл {input_path} не найден")

    except Exception as e:
        print(f"Ошибка при обработке файлов: {e}")


if __name__ == "__main__":  # Обозначаем, что функция main будет выполняться первой
    main()
