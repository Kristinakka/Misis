from pathlib import Path
import csv
import sys
import json

# Добавляем путь для работы с CSV, импортируем функции
sys.path.append(r"C:\VS\VS_MISIS\Misis\src\lab04")
from io_txt_csv import write_csv


def json_to_csv(json_path, csv_path):

    # Проверяем расширение файла
    if json_path[-4:] != "json":
        return f"TypeError! Неверный формат файла {json_path}"

    json_path = Path(json_path)
    csv_path = Path(csv_path)

    # Проверяем существование JSON файла
    if not json_path.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")

    try:
        # Читаем данные из JSON
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

    except json.JSONDecodeError:
        raise ValueError(
            "Ошибка декодирования JSON: файл пуст или имеет неправильный формат"
        )

    # Проверяем структуру данных
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if not data:
        raise ValueError("JSON файл пуст")

    # Проверяем, что все элементы - словари
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы в JSON должны быть словарями")

    # Получаем заголовки из ключей первого словаря
    header = tuple(data[0].keys())

    # Формируем строки данных
    rows = [tuple(item.values()) for item in data]

    # Записываем в CSV
    write_csv(rows, csv_path, header)

    return "Файл успешно создан"


def csv_to_json(csv_path, json_path):

    # Проверяем расширение файла
    if not csv_path.lower().endswith(".csv"):
        return f"TypeError! Неверный формат файла {csv_path}"

    csv_path = Path(csv_path)
    json_path = Path(json_path)

    # Проверяем существование CSV файла
    if not csv_path.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    try:
        # Читаем данные из CSV
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)

    except Exception as e:
        raise FileNotFoundError(f"Ошибка при чтении CSV файла: {e}")

    # Проверяем, что файл не пустой
    if not rows:
        raise ValueError("CSV файл пуст")

    # Проверяем наличие заголовков
    if not csv_reader.fieldnames:
        raise ValueError("CSV файл не содержит заголовков")

    # Записываем в JSON с нормальным форматированием
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(rows, json_file, indent=4, ensure_ascii=False)

    return "Файл успешно создан"


# Примеры использования
if __name__ == "__main__":
    # Тестирование JSON to CSV
    try:
        result1 = json_to_csv(
            "C:\VS\VS_MISIS\Misis\src\lab05\Test1.json",
            "C:\VS\VS_MISIS\Misis\src\lab05\Test1.csv",
        )
        print(result1)
    except Exception as e:
        print(f"Ошибка при конвертации JSON в CSV: {e}")

    # Тестирование CSV to JSON
    try:
        result2 = csv_to_json(
            "C:\VS\VS_MISIS\Misis\src\lab05\Test2.csv",
            "C:\VS\VS_MISIS\Misis\src\lab05\Test2.json",
        )
        print(result2)
    except Exception as e:
        print(f"Ошибка при конвертации CSV в JSON: {e}")
