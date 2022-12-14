# ===================================================================================
# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
#       возвращает словарь, ключи — первые буквы фамилий, значения — словари,
#       реализованные по схеме предыдущего задания.
# in >> "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
#
# out >>   {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
#           'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']},
#           'И': {'И': ['Илья Иванов']},
#           'В': {'Ю': ['Юнона Ветрякова']}}
# --------------------------------------------------------------------------------------

# ===== Вариант преподавателя ==========
def create_dictionary(ls: list):
    dc = {}
    for sn in ls:
        dc.setdefault(sn.split()[1][0], {}).setdefault(sn.split()[0][0], []).append(sn)
    return dc


# -------------------------------------

# ========== пока не допилил свое решение по аналогии с заданием 6_4 ===============================
# ========== временно вернул к варианту функции выше ===============================================
def create_dict(ls: list):
    dc = {}
    for i in ls:
        ch = i.split()[1][0]
        ch2 = i.split()[0][0]
        dc.setdefault(ch, {}).setdefault(ch2, []).append(i)
    return dc


iput_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
             "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]
print(f"Формируем словарь из строк {iput_list}")
print(create_dict(iput_list))
