import func_prog as fg

list_menu_prim = ["", "1;Сотрудники", "2;Автопарк", "3;Маршруты", "4;Автосервис", "5;Справочники", "0;Выход"]
list_menu_worker = ["",
                    "1;Добавить сотрудника",
                    "2;Посмотреть сотрудников по имени",
                    "3;Посмотреть сотрудников по фамилии",
                    "4;Редактировать данные сотрудника",
                    "5;Посмотреть всех сотрудников",
                    "0;Назад"
                    ]


def strin_rep(st: str):
    st = st.replace("-", "").replace(",", ".").split(".")[0]
    return st


def input_mode(lst):
    for i, m in enumerate(lst):
        if i > 0:
            print(f'{m.split(";")[0]} - {m.split(";")[1]}')
    while True:
        inp = strin_rep(input())
        if inp.isdigit() and int(inp) >= 0:
            mode = int(inp)
            if 0 <= mode < len(lst)+1:
                return mode
            else:
                print("Неверный ввод!")


def menu():
    while True:
        mode = input_mode(list_menu_prim)
        if mode == 0:
            exit("До свидания!")
        elif mode == 1:
            workers()
        elif mode == 2:
            fg.view_autopark()
        elif mode == 3:
            fg.view_route()
        elif mode == 4:
            fg.view_service()
        elif mode == 5:
            fg.view_references()


def workers():
    while True:
        oper = input_mode(list_menu_worker)
        if not oper:
            menu()
        elif oper == 1:
            fg.add_worker()
        elif oper == 2:
            fg.view_search_fist_name()
        elif oper == 3:
            fg.view_search_last_name()
        elif oper == 4:
            fg.edit_worker()
        elif oper == 5:
            fg.view_all_workers()




