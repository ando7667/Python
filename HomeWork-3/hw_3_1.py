# ==============================================================
# 1. Задайте список, состоящий из произвольных чисел,
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8
# --------------------------------------------------------------
import random


def create_rnd_list(num):
    lst = []
    for i in range(num):
        lst.append(random.randint(1, 100))
    return lst


def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number


def summ_element_odd_pos(sp: list):
    summa = 0
    for i in range(0, len(sp), 2):
        summa += sp[i]
    return summa


spisok = create_rnd_list(input_int())
print("Список элементов: ", spisok)
print("Сумма элементов списка на нечетных позициях: ", summ_element_odd_pos(spisok))
