# =============================================================================
# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#       Входные и выходные данные хранятся в отдельных текстовых файлах.
# in >> Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out >> aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaavvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#        vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# ---------------------------------------------------------------------------------
import os
from itertools import groupby


def check_file(f1: str, f2: str, f3: str):
    if os.access(f1, os.F_OK) == True:
        if os.access(f2, os.F_OK) == True:
            if os.access(f3, os.F_OK) == True:
                return True
    else:
        return False


def rle_encode(f1: str, f2: str):
    with open(f1, "r", encoding="utf-8") as f1, \
            open(f2, "w", encoding="utf-8") as f2:
        for i in f1:
            f2.write("".join([f"{len(tuple(group))}{key}" for key, group in groupby(i)]))


def rle_decode(f3: str):
    with open(f3, "r", encoding="utf-8") as f3:
        for i in f3:
            count = ""
            st = ""
            for k in i.strip():
                if k.isdigit():
                    count += k
                else:
                    st += k * int(count)
                    count = ""
            print(st)


file1 = input("Введите имя первого файла с записями многочленов ( t1.txt ): ")
file2 = input("Введите имя второго файла с записями многочленов ( z1.txt ): ")
file3 = input("Введите имя второго файла с записями многочленов ( z1.txt ): ")
if check_file(file1, file2, file3):
    rle_encode(file1, file2)
    rle_decode(file3)
else:
    print("Не могу найти один из файлов!")
