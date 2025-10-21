from A import normalize, tokenize, count_freq, top_n

fl = open("C:\VS\VS_MISIS\Misis\src\lab03\\text", encoding="utf-8").read()
fl = normalize(fl, True, True)

print("\n")

print(fl)

print("\n")

print(f"Всего слов: {len(tokenize(fl))}")
print(f"Уникальных слов: {len(set(tokenize(fl)))}")
print("Top-5:")
for i in top_n(count_freq(tokenize(fl)), 5):
    print(f"{i[0]}:{i[1]}")
