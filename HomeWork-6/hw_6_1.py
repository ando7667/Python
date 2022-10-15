# ===================================================================================
# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
#    которых больше предыдущего элемента. Use comprehension.
# in >> 9
# out >> [15, 16, 2, 3, 1, 7, 5, 4, 10]
#        [16, 3, 7, 10]
#
# in >> 10
# out >> [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
#        [24, 15, 23, 25]
# ------------------------------------------------------------------------------------

from random import sample


def input_int():
    inp = input("Введите число: ")
    if inp.isdigit() and int(inp) > 0:
        return int(inp)


def gen_list_number(num):
    return sample(range(num), num)


def more_previous(ls: list):
    return [ls[n] for n in range(1, len(ls)) if ls[n] > ls[n - 1]]


ls_number = gen_list_number(input_int())
print(ls_number)
print(more_previous(ls_number))
