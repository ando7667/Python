# ========================================================
# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# Простые делители числа
#
# in >> 54
# out >> [2, 3, 3, 3]
#
# in >> 9990
# out >> [2, 3, 3, 3, 5, 37]
#
# in >> 650
# out >> [2, 5, 5, 13]
# --------------------------------------------------------------------
def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number


def factors(num):
    prime_divisors = []
    pd = 2
    while num > 1:
        if num % pd == 0:
            prime_divisors.append(pd)
            num /= pd
        else:
            pd += 1
    return prime_divisors


print(factors(input_int()))
