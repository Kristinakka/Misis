ch1 = input("a:")
ch2 = input("b:")
ch1, ch2 = float(ch1.replace(",", ".")), float(ch2.replace(",", "."))
sum = ch1 + ch2
sr = sum / 2
print(sum)
print(sr)
