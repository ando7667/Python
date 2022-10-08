#  ===========================================================
# Создайте список, в который попадают числа,
#  описывающие возрастающую последовательность.
#  Порядок элементов менять нельзя.
# ------------------------------------------------------------
from random import choices


def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number


def fill_list(num: int):
    return choices(range(num * 2), k=num)


def find_sublist(lst: list):
    res = []
    for i in range(len(lst)):
        cur = lst[i]
        cur_lst = [cur]
        for k in range(i, len(lst)):
            if lst[k] > cur:
                cur_lst.append(lst[k])
                cur = lst[k]
        if len(cur_lst) > 1:
                res.append(cur_lst)
    return res


array = fill_list(input_int())
print(array)
array2 = find_sublist(array)
print(array2)
