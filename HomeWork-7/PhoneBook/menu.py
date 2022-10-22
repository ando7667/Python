import file_oper as fo


def strin_rep(st: str):
    st = st.replace("-", "").replace(",", ".").split(".")[0]
    return st


def input_data():
    data_rec = []
    last_name = input('Введите фамилию: ')
    data_rec.append(last_name)
    first_name = input('Введите имя: ')
    data_rec.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    data_rec.append(phone_number)
    description = input('Введите описание: ')
    data_rec.append(description)
    return data_rec



def input_mode():
    print("Работа с телефонной книгой:\n"
          "1 - Посмотреть список\n"
          "2 - Добавить запись\n"
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


def menu():
    f1 = 'Phonebook.csv'
    if not fo.check_file(f1):
        fo.creat_file()

    while True:
        mode = input_mode()
        if mode == 2:
            rec = input_data()
            fo.writing_scv(rec)
        if mode == 1:
            phone = fo.read_scv()
        if mode == 0:
            exit("До свидания!")

