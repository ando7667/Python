# =====================================================================================
# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# in  >> 5
# out >>    [5.16, 8.62, 6.57, 7.92, 9.22]
#           Min: 0.16, Max: 0.92. Difference: 0.76
# in  >>  3
# out >>    [9.26, 8.5, 1.14]
#           Min: 0.14, Max: 0.5. Difference: 0.36
# ------------------------------------------------------------------------------------
import random


def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number


def create_float_rnd_list(num):
    lst = []
    for i in range(num):
        lst.append(round(random.random() * 10, 2))
    return lst


def find_min_fract_part_number(sp: list):
    min_num = sp[0]
    count = len(sp)
    for i in range(0, count):
        if sp[i] % 1 < min_num:
            min_num = round(sp[i] % 1, 2)

    return min_num


def find_max_fract_part_number(sp: list):
    max_num = 0
    count = len(sp)
    for i in range(0, count):
        if sp[i] % 1 > max_num:
            max_num = round(sp[i] % 1, 2)

    return max_num


def diff_min_max(inmin, inmax):
    return round(inmax - inmin, 2)


num = input_int()
print(num)
spisok = create_float_rnd_list(num)
print(spisok)
min_num = find_min_fract_part_number(spisok)
max_num = find_max_fract_part_number(spisok)
print("Min:", min_num, ", Max:", max_num, ", Difference:", diff_min_max(inmin=min_num, inmax=max_num))
