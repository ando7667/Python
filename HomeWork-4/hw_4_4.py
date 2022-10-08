# ============================================================================
# 4.* Задана натуральная степень k. Сформировать случайным образом список
#     коэффициентов (от 0 до 10) многочлена, записать в файл полученный
#     многочлен не менее 3-х раз.
# in >>
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
#
# in
# 0
# -1
# 4
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
# ---------------------------------------------------------

from random import choice


def input_int():
    number = int(input("Введите целое число: ").replace(",", ".").split(".")[0])
    return number


def polynomial(num: int):
    if num < 1:
        return 0

    st = ""
    sign = "-+"
    lst = range(0, 10)

    for i in range(num, 0, -1):
        v = choice(lst)
        if v:
            st += f"{v}*x^{i} {choice(sign)} "

    st += f"{choice(lst)} = 0\n"
    with open("polynomial.txt", "a", encoding="utf-8") as file:
        file.write(st)


col = int(input("Введите количество многочленов: ").replace("-", ""))
for i in range(col):
    polynomial(input_int())
