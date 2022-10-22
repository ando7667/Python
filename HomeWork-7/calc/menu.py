import my_math as m
from input import input_data as inpd
from logger import logger_history as lm

oper_list = [m.sum, m.sub, m.mult, m.div, m.pow, m.div_compl, m.remainder_div, m.sqrt_pow]


def strin_rep(st: str):
    st = st.replace("-", "").replace(",", ".").split(".")[0]
    return st


def input_mode():
    print("Задайте режим вычислений:\n"
          "1 - для обычных чисел\n"
          "2 - для комплексных чисел\n"
          "0 - Выход\n")
    mode = -1
    while mode:
        inp = strin_rep(input())
        if inp.isdigit() and int(inp) >= 0:
            mode = int(inp)
            if mode == 0:
                exit("До свидания!")
            if 0 <= mode < 3:
                return mode
            else:
                mode = -1
                print("Неверный ввод!")
                lm("Введен неверный пункт меню", "", "")


def input_operation(mode: int):
    print("Выберите операцию:\n"
                "1. Сложение\n"
                "2. Вычитание\n"
                "3. Умножение\n"
                "4. Деление\n"
                "5. Ввозведение в степень")
    if mode == 1:
        print("6. Деление на целое\n"
                  "7. Остаток от деления\n"
                  "8. Корень числа со степенью")
    print("0. Выход\n")
    op = -1
    while op:
        inp = strin_rep(input())
        if inp.isdigit() and int(inp) >= 0:
            op = int(inp)
            if op == 0:
                exit("До свидания")
            if 0 <= op < 9 and mode == 1:
                return op
            if 0 <= op < 6 and mode == 2:
                return op
            else:
                op = -1
                print("Неверный ввод!")
                lm("Введен неверный пункт меню", "", "")


def menu():
    while True:
        mode = input_mode()
        operation = input_operation(mode)
        num1, num2 = inpd(mode, operation)
        if num1 != 0 and num2 != 0:
            m.fun(oper_list[operation-1], num1, num2)



