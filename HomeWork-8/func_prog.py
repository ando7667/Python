import file_oper as fo
import menu as m
import logger as lg


def input_data():
    data_rec = []
    last_name = input('Введите Фамилию: ')
    data_rec.append(last_name)
    first_name = input('Введите Имя: ')
    data_rec.append(first_name)
    patronymic = input('Введите Отчество: ')
    data_rec.append(patronymic)
    year_birth = ''
    valid = False
    while not valid:
        try:
            year_birth = input('Введите год рождения: ')
            if len(year_birth) != 4:
                print('В году должно быть 4 цифры.')
            else:
                year_birth = int(year_birth)
                valid = True
        except:
            print('год рождения должен состоять только из цифр.')
    data_rec.append(year_birth)
    prof = fo.read_scv('profession.csv')
    if len(prof) > 0:
        print("Выбирите профессию сотрудника")
        pf = m.input_mode(prof)
        data_rec.append(pf)
    shift = fo.read_scv('shift.csv')
    if len(shift) > 0:
        print("Выбирите смену для сотрудника")
        sh = m.input_mode(shift)
        data_rec.append(sh)

    return data_rec

# ножно находить мах id в файле, делать инкремент и добавлять к rec спереди
# также нужно переименовать заголовки столбцов в файлах csv в одно слово и в латиницу
def add_worker():
    rec = input_data()
    print(rec)
    fo.writing_scv(rec, 'worker.csv')
    return 1


def view_search_last_name():
    work = fo.read_scv('worker.csv')
    last_name = input('Введите буквы фамилии: ')
    l = [n for n, x in enumerate(work) if x == last_name]
    print(l)
#    print("Фукнция пока не реализована")
    return 1


def view_search_fist_name():
    print("Фукнция пока не реализована")
    return 1


def view_all_workers():
    print("Таблица сотрудников\n"
          f"{'=' * 30}")
    wk = []
    work = fo.read_scv('worker.csv')
    shift = fo.read_scv('worker.csv')
    for w in work:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Вывод таблицы сотрудников", "", "")
    return 1


def edit_worker():
    fo.search_max_id('worker.csv')
    print("Фукнция пока не реализована")
    return 1


def view_autopark():
    print("Таблица автотехники парка\n"
          f"{'=' * 30}")
    ap = fo.read_scv('autopark.csv')
    for w in ap:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Вывод таблицы автотехники парка", "", "")


def view_route():
    print("Таблица маршрутов\n"
          f"{'=' * 30}")
    rt = fo.read_scv('route.csv')
    for w in rt:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Вывод таблицы маршрутов", "", "")


def view_service():
    print("Таблица сервисного обслуживания\n"
          f"{'=' * 30}")
    sr = fo.read_scv('service.csv')
    for w in sr:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Вывод таблицы сервисного обслуживания", "", "")


def view_references():
    print("Справочник профессий\n"
          f"{'=' * 30}")
    pr = fo.read_scv('profession.csv')
    for w in pr:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    print("Справочник статусов\n"
          f"{'=' * 30}")
    st = fo.read_scv('status.csv')
    for w in st:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    print("Справочник причин обслуживания техники\n"
          f"{'=' * 30}")
    sr = fo.read_scv('reasons_maintenance.csv')
    for w in sr:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Вывод всех справочников", "", "")
