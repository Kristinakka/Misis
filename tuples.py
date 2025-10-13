def format_record(tup):
    if type(tup) != tuple:
        return "TypeError"

    if len(tup) != 3:
        return "ValueError"

    fio = tup[0].split()
    fio_itog = (
        f"{fio[0][0].upper()}{fio[0][1:]} {fio[1][0].upper()}.{fio[2][0].upper()}., "
    )

    group = f"гр. {tup[1]}, "

    gpa = f"GPA {tup[2]:.2f}."

    return fio_itog + group + gpa


print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
