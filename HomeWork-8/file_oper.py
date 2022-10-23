import os
import random

import logger as lg

file = ['worker.csv', 'profession.csv', 'status.csv', 'autopark.csv', 'service.csv', 'shift.csv',
        'reasons_maintenance.csv', 'route.csv', 'history.log']

file_head = [
    'id сотрудника;фамилия;имя;отчество;год рождения;id профессии;id смены\n',
    'id;профессия\n',
    'id;статус\n',
    'id техники;вид;марка;гос.номер;год ввода в экспуатацию;id статуса\n',
    'id обслуживания;дата начала работ;дата окончания работ;id сотрудника;id техники;id причины;Комментарий\n',
    'id;смена;время начала смены;время конца смены\n',
    'id причины;Причина\n',
    'id;Номер маршрута;id техники;id сотрудника (водитель);id сотрудника (контролер);Начало 1го рейса;Начало последнего рейса;Время в пути,мин;Старт маршрута;Конец маршрута\n',
    ''
]

# что-то не работает
def count_lines(filename, chunk_size=1 << 13):
    with open(filename) as fl:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: fl.read(chunk_size), ''))


def search_max_id(fl: str):
    if check_file(fl):
        with open(fl, 'r', encoding='utf-8') as f1:
            st = []
            max = 0
#            for x in f1:
#                st = x.split(";")
#                if i == 0:
#                    max = x[0]
#                else:
#                    x[0] > max
#                    max = x[0]



def check_file(f1: str):
    if os.access(f1, os.F_OK):
        return True
    else:
        return False


def writing_scv(rec: list, fl: str):
    if check_file(fl):
#        count = count_lines(fl)
        with open(fl, 'a', encoding='utf-8') as f1:
#            count = len(f1.readlines())
#            rec.insert(0, count+1)
            # временная генерация случайного ид для сотрудника
            rec.insert(0, random.randint(20, 100))
            f1.write(f'{rec[0]};{rec[1]};{rec[2]};{rec[3]};{rec[4]};{rec[5]};{rec[6]}\n')
            lg.logger_history("Запись нового сотрудника", f"{rec[1]} {rec[2]} {rec[3]}", "удачно")
    else:
        print(f"файл {fl} не найден!")
        lg.logger_history("Новый сотрудник не сохранен", f"{rec[1]} {rec[2]} {rec[3]}", "Файл не найден")


def creat_file():
    for i, f in enumerate(file):
        if not check_file(f):
            with open(f, 'w', encoding='utf-8') as f1:
                f1.write(file_head[i])
                lg.logger_history("Создан отсутствующий файл ", f"{f}", "")


def read_scv(fl: str):
    if check_file(fl):
        with open(fl, 'r', encoding='utf-8') as f1:
            return f1.readlines()
    else:
        print(f"файл {fl} не найден!")
        lg.logger_history("Ошибка чтения файла", f"{fl}", "не найден")
        return []
