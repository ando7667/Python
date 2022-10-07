# ================================================================================
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in  >> 88
# out >> 1011000
#
# in >> 11
# out >> 1011
# --------------------------------------------------------------------------------
def input_int():
    number = int(input("Введите целое число: ").replace("-", "").replace(",", ".").split(".")[0])
    return number



def converting_integer_to_binary(num: int):
    result = ""
    if num == 0:
        return 0
    while num:
        result = str(num % 2) + result
        num //= 2
    return result



num = input_int()
print("Вы ввели число: ", num)
print("В двоичном виде: ", converting_integer_to_binary(num))
