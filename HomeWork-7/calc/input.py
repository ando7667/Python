from logger import logger_history as ld


def input_data(mode: int, oper: int):
    try:
        if mode == 1:
            if oper != 5 and oper != 8:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            else:
                num1 = float(input("Введите число: "))
                num2 = int(input("Введите степень: "))
        elif mode == 2:
            if oper < 5:
                num1 = complex(float(input("Введите первое значение для первого комплексного числа: ")),
                               float(input("Введите второе значение для первого комплексного числа: ")))

                num2 = complex(float(input("Введите первое значение для второго комплексного числа: ")),
                               float(input("Введите второе значение для второго комплексного числа: ")))
            elif oper == 5:
                num1 = complex(float(input("Введите первое значение для первого комплексного числа: ")),
                               float(input("Введите второе значение для первого комплексного числа: ")))
                num2 = int(input("Введите степень: "))

    except:
        print("Вы ввели недопустимые символы")
        ld("Внимание", "введено недопустимое значение", "")
#        input_data(mode, oper)
        return 0, 0

    else:
        return num1, num2

