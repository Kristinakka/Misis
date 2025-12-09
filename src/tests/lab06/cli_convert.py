import argparse
import sys

sys.path.append(r"C:\VS\VS_MISIS\Misis\src\lab05")
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.out)

    elif args.command == "csv2json":
        csv_to_json(args.input, args.out)

    elif args.commnd == "csv2xlsx":
        csv_to_xlsx(args.input, args.out)


if __name__ == "__main__":
    main()

# python C:\VS\VS_MISIS\Misis\src\lab06\cli_convert.py json2csv --in C:\VS\VS_MISIS\Misis\data\lab06\in\my.json --out C:\VS\VS_MISIS\Misis\data\lab06\out\new.csv
# python3 C:\VS\VS_MISIS\Misis\src\lab06\cli_convert.py csv2json --in C:\VS\VS_MISIS\Misis\data\lab06\in\my.csv --out C:\VS\VS_MISIS\Misis\data\lab06\out\new.csv
# python3 C:\VS\VS_MISIS\Misis\src\lab06\cli_convert.py csv2xlsx --in C:\VS\VS_MISIS\Misis\data\lab06\in\my.csv --out C:\VS\VS_MISIS\Misis\data\lab06\out\new.xlsx
