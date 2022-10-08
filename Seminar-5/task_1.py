#  ===========================================================
#  Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.
# -----------------------------------------------------------
from secrets import choice


def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number


def fill_list(num: int):
    array = [i for i in range(num + 1)]
    array.remove(choice(array))
    return array


def check_number(array):
    index = 0
    for i in range(1, len(array)):
        if array[i] - 1 != array[i - 1]:
            return array[i - 1] + 1
    return -1


array = fill_list((int(input_int())))
print(array)
print(check_number(array))
