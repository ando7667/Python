# ===============================================================
# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности
# в том же порядке.
# in >> 7
# out >> [4, 5, 3, 3, 4, 1, 2]
#        [5, 1, 2]
#
# in >> -1
# out >> Negative value of the number of numbers!
#        []
#
# in >> 10
# out >> [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#        [6, 2, 3, 0, 9]
# ------------------------------------------------------------
import random


def input_int():
    number = int(input("Введите целое число: ").replace(",", ".").split(".")[0])
    if number < 0:
        exit("Negative value of the number of numbers!")
    return number


def create_rnd_list(num: int):
    lst = []
    for i in range(num):
        lst.append(random.randint(1, 10))
    return lst


def search_nonrepeat_elements(lst: list):
    search = []
    for i in lst:
        if lst.count(i) == 1:
            search.append(i)

    return search


arr = create_rnd_list(input_int())
print(arr)
print(search_nonrepeat_elements(arr))
