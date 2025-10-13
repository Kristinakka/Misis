def transpose(nums):  # Функция
    ans = []  # наш будущий ответ
    if nums == []:  #  Если поступающий список пустой
        return nums  # Возвращаем пустой список

    dlina = len(nums[0])  # Создали переменную длинны первой строки

    for k in nums[1:]:  # Пока k в списке (то есть k принимает значения строк матрицы)
        if dlina != len(k):  # Если длина строки k не равна длине первой строки списка
            return "ValueError"  # Возвращаем ошибку

    for i in range(
        dlina
    ):  # Пока i на числовом отрезке от 0 до dlina не включительно (0, 1)
        a = []  # Создали переменную для формируемых новых строк
        for j in nums:  # Пока j в списке (то есть j принимает значения строк матрицы)
            a.append(
                j[i]
            )  # Добавляем i-ый элемент элемента j (то есть, элемент индекса i строки j)
        ans.append(a)
    return ans


print(transpose([[1, 2, 3]]))


def row_sums(nums):
    ans = []
    if nums == []:
        return nums

    dlina = len(nums[0])

    for k in nums[1:]:
        if dlina != len(k):
            return "ValueError"

    for i in nums:
        a = []
        a.append(sum(i))
        ans.append(a)
    return ans


print(row_sums([[-1, 1], [10, -10]]))


def col_sums(nums):
    if nums == []:
        return nums

    dlina = len(nums[0])
    summ = [0] * dlina

    for k in nums[1:]:
        if dlina != len(k):
            return "ValueError"

    for i in nums:
        for j in range(dlina):
            summ[j] += i[j]
    return summ


print(col_sums([[1, 2, 3], [4, 5, 6]]))
