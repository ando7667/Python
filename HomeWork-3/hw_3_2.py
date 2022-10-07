# ====================================================================
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in  >> 4
# out >>    [2, 5, 8, 10]
#           [20, 40]
# in >> 5
# out >>    [2, 2, 4, 8, 8]
#           [16, 16, 4]
# --------------------------------------------------------------------
import random


def create_rnd_list(num):
    lst = []
    for i in range(num):
        lst.append(random.randint(1, 10))
    return lst


def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number

def multip_pairs_list_numbers(sp: list):
    mult = []
    count_max = int(len(sp))
    count = int(count_max/2)
    for i in range(0, count):
        mult.append(sp[i] * sp[count_max-i-1])
    if count_max % 2:
        mult.append(sp[count_max // 2])
    return mult


num = input_int()
print(num)
spisok = create_rnd_list(num)
print(spisok)
print(multip_pairs_list_numbers(spisok))
