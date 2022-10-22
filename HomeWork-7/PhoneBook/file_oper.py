import os

file = 'Phonebook'


def check_file(f1: str):
    if os.access(f1, os.F_OK):
        return True
    else:
        return False


def writing_scv(rec, file: str = file):
    file += ".csv"
    if check_file(file):
        with open (file, 'a', encoding = 'utf-8') as f1:
            f1.write(f'{rec[0]};{rec[1]};{rec[2]};{rec[3]}\n')
    else:
        print(f"файл {file} не найден!")

def creat_file(file: str = file):
    file += ".csv"
    with open (file, 'w', encoding = 'utf-8') as f1:
        f1.write(f'Фамилия;Имя;Номер телефона;Описание\n')


def read_scv (file: str = file):
    file += ".csv"
    if check_file(file):
        with open (file, 'r', encoding = 'utf-8') as f1:
            phone = f1.readlines()
            for x in phone:
                print(x)
            return phone
    else:
        print(f"файл {file} не найден!")
        return []
