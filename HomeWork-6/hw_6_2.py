# ===================================================================================
# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in >> 100
# out >> [20, 21, 40, 42, 60, 63, 80, 84, 100]
#
# in >> 424
# out >> [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180,
# 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357,
# 360, 378, 380, 399, 400, 420]
# ------------------------------------------------------------------------------------


def input_int():
    inp = input("Введите число: ").replace("-", "").replace(",", ".").split(".")[0]
    if inp.isdigit() and int(inp) > 0:
        return int(inp)


def multiple_filter(num: int, a: int = 20, b: int = 21):
    return [n for n in range(20, num+1) if n % a == 0 or n % b == 0]


print(multiple_filter(input_int()))
