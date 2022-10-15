# ===========================================================
# 1. Напишите программу, удаляющую из текста все слова,
#       содержащие "абв". В тексте используется разделитель пробел.
# in >> Number of words: 10
# out >> авб абв бав абв вба бав вба абв абв абв
#        авб бав вба бав вба
#
# in >> Number of words: 6
# out >> ваб вба абв ваб бва абв
#        ваб вба ваб бва
# -----------------------------------------------------------
import random

def gen_str(col: int, st: str):
    spisok = []
    for i in range(col):
        word = random.sample(st, 3)
        spisok.append("".join(word))
    return " ".join(spisok)


def remove_word(st: list, filter: str):
    st = " ".join(st.replace(filter, "").split())
    return st


set_letters = "абв"
сс = int(input("введите количество слов: ").replace("-", "").replace(",", ".").split(".")[0])
ran_text = gen_str(сс, set_letters)
print(ran_text)
print(remove_word(ran_text, set_letters))
