import re


def normalize(text, casefold, yo2e):

    if casefold == True:
        text = text.casefold()

    if yo2e == True:
        text = text.replace("ё", "е").replace("Ё", "Е")

        text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
        text = text.strip()
    return text


# print(normalize("ПрИвЕт\nМИр\t", casefold=True, yo2e=True))


def tokenize(text):
    lst = re.findall(r"[\w-]+", text)
    answer = []
    for i in lst:
        if i[0].isdigit() or i[0].isalpha():
            answer.append(i)
    return answer


# print(tokenize("hello,world!!!"))


def count_freq(tokens):
    ans = {}
    for i in tokens:
        ans[i] = tokens.count(i)
    return ans


# print(count_freq(["a", "b", "a", "c", "b", "a"]))


def top_n(freq, n):
    answ = sorted(list(freq.items()), key=lambda x: (-x[1], x[0]))

    return answ[:n]


print(top_n(count_freq(["a", "b", "c", "c", "b", "c"]), 3))
