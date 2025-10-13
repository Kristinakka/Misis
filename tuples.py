def format_record(tup):
    if type(tup) != tuple:
        return "TypeError"

    if len(tup) != 3:
        return "ValueError"

    fio = tup[0].split()
    fio_itog = f"{fio[0][0].upper()}{fio[0][1:]} "

    for i in range(1, len(fio)):
        fio_itog += f"{fio[i][0].upper()}."

    fio_itog += ","

    group = f" гр. {tup[1]}, "

    gpa = f"GPA {tup[2]:.2f}."

    return fio_itog + group + gpa


print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
