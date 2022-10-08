'''Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).'''
import math
quarter = int(input('Введите номер четверти: '))
match quarter:
    case 1:
        print('x > 0')
        print('y > 0')
    case 2:
        print('x < 0')
        print('y > 0')
    case 3:
        print('x < 0')
        print('y < 0')
    case 4:
        print('x > 0')
        print('y < 0')

