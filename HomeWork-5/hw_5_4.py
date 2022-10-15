# =======================================================================================
# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
# ----------------------------------------------------------------------------------------
import random

sweets = 117
max_sweets_run = 28
result = sweets


def menu():
    inp = False
    while not inp:
        pl = int(input("Выбирите вариант игры:\n"
                       "1. Игрок против Игрока\n"
                       "2. Игрок против Бота\n"
                       "0. Не хочу играть\n").replace("-", "").replace(",", ".").split(".")[0])
        if pl > 2:
            print("Ввели неверный код")
        else:
            inp = True
    return pl


def rnd_player():
    return random.randint(0, 1)


def input_player(player: int):
    global result
    inp = False
    while not inp:
        pl = input(f"Игрок {player + 1} возьмите количество конфет от до {max_sweets_run}: ")
        if pl.isdigit() and int(pl) in range(1, max_sweets_run + 1):
            pl = int(pl)
            inp = True
    return pl


def input_bot():
    return random.randint(1, max_sweets_run)


def game(mn: int):
    global result
    player = rnd_player()
    game_st = True
    while game_st:
        if mn == 2 and player:
            num = input_bot()
        else:
            num = input_player(player)
        if result >= num:
            result -= num
            if result > 0:
                print(f"На столе осталось {result} конфет")
                player = not player
            else:
                game_st = False
        else:
            game_st = False

    print(f"На столе не осталось конфет!")
    print(f"Выиграл Игрок {player + 1} ! {chr(127874)}")


print("Игра в конфетки")
mn = menu()
if mn == 0:
    print("Досвидания!")
    exit()
else:
    game(mn)
