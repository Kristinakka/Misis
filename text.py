def normalize(text, casefold, yo2e):

    if casefold == True:
        text = text.casefold()

    if yo2e == True:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")

        text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
        text = text.strip()
    return text


print(normalize("ПрИвЕт\nМИр\t", casefold=True, yo2e=True))
