""" Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом" """

import os
import random
def player_take(num):
    global all_candys
    global last_player
    take_candy = 0
    while  take_candy not in range(1,max_take + 1) :
        take_candy = int(input(f'Сколько конфет берет игрок {num}: '))
        if all_candys - take_candy < 0:
            print('Столько конфет не осталось...')
            take_candy = 0
    all_candys -= take_candy
    last_player = num

os.system('cls')
print('1 - 2 игрока')
print('2 - игра с компьютером')
print('3 - игра с умным компьютером')
game_mode = int(input('Выберите режим: '))
all_candys = 56
max_take = 12
if game_mode == 1:
    lot = random.randint(1,2)
    
    while all_candys > 0:
        os.system('cls')
        print(f'Осталось {all_candys} конфет')
        print(f'Ходит игрок {lot}')
        player_take(lot)
        if lot == 1: lot = 2
        else: lot = 1
        
    print(f'Игрок {last_player} выиграл')

if game_mode == 2:
    lot = random.randint(1,2)
    comp_take = 0
    while all_candys > 0:     
        print(f'Осталось {all_candys} конфет')
        if lot == 2:
            comp_take = random.randint(1,max_take)
            if all_candys <= max_take:
                comp_take = all_candys    
            print(f'Компьтер взял {comp_take} конфет')
            all_candys -= comp_take
            last_player = lot
            lot = 1
        else:
            player_take(lot)
            lot = 2
            os.system('cls')
    if last_player == 1:
        print('Вы выиграли!!!')
    else:
        print('Компьютер выиграл!')
    
if game_mode == 3:
    lot = random.randint(1,2)
    comp_take = 0
    while all_candys > 0:     
        print(f'Осталось {all_candys} конфет')
        if lot == 2:
            comp_take = all_candys % (max_take + 1)
            if comp_take == 0: comp_take = 1
            if all_candys <= max_take:
                comp_take = all_candys    
            print(f'Компьтер взял {comp_take} конфет')
            all_candys -= comp_take
            last_player = lot
            lot = 1
        else:
            player_take(lot)
            lot = 2
            os.system('cls')
    if last_player == 1:
        print('Вы выиграли!!!')
    else:
        print('Компьютер выиграл!')