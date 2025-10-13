name = input("ФИО: ")
p = name.split()
print(f"Инициалы:{p[0][0] + p[1][0] + p[2][0]}")
print(f"Длина(символов):{len(p[0]) + len(p[1]) + len(p[2])}")
