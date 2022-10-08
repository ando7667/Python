# =========================================================
#  Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.
#  in >> 11 23 90 -8 12 7 45 -44
#  out >> -44 90
#
# in >> 1, 6. 8: 9! -4
# out >> -4 9
#
# in >> 1 u 6 i 9  или  in >> 7t 5d 7
# out >> "The data is incorrect"
# -------------------------------------------------------

def my_func(string_val):
    for index in string_val:
        if not index.replace("-", "").isdigit():
            return []
    return string_val


def min_sum(val):
    art = my_func(val)
    if art:
        return min(art, key=int), max(art, key=int)
    else:
        return []

print("Введите строку чисел через пробел: ")
print(min_sum(input().split()))