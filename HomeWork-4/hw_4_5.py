# ========================================================================
# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
#       Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
# "poly.txt"
# "poly_2.txt"
#
# out
# The contents of the files do not match!
# -----------------------------------------------------------------------
import os

def check_file(f1: str, f2: str):
    if os.access(f1, os.F_OK) == True:
        if os.access(f2, os.F_OK) == True:
            return True
    else:
        return False

def sum_file_pol(f1: str, f2: str):
    with open(f1, "r", encoding="utf-8") as f1, \
            open(f2, "r", encoding="utf-8") as f2:
        file1 = f1.readlines()
        file2 = f2.readlines()
        if len(file1) != len(file2):
            print("В выбранных файлах разное количество строк с многочленами !")
        else:
            sum = []
            for i, v in enumerate(file1):
                sum.append(f"{v[:-5]} + {file2[i]}")

            with open("sum_poly.txt", "a", encoding="utf-8") as file3:
                file3.writelines(sum)



file1 = input("Введите имя первого файла с записями многочленов ( p1.txt ): ")
file2 = input("Введите имя второго файла с записями многочленов ( p2.txt ): ")
if check_file(file1, file2):
    sum_file_pol(file1, file2)
else:
   print("Не могу найти один из файлов!")
