# =====================================================================================
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in >>  8
# out >>    -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in >> 5
# out >>    5 -3 2 -1 1 0 1 1 2 3 5
# -------------------------------------------------------------------------------------

def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number


def nega_fibonachi(num: int):
    fib = [0]
    fib1 = fib2 = 1

    for i in range(num):
        fib.append(fib1)
        fib.insert(0, fib1 * (-1) ** i)
        fib1, fib2 = fib2, fib1 + fib2

    return fib


num = input_int()
print(num)
print(*nega_fibonachi(num))
