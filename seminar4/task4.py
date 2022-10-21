# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

import random
def polynom_gen(k):

    degree = {
        '0': '\u2070',
        '1': '\u00B9',
        '2': '\u00B2',
        '3': '\u00B3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079'
            }
    first=True
    result=''
    for i in range(k, -1, -1):
        coefficient = random.randint(-100,100)
        if coefficient == 0:
            continue
        if abs(coefficient) == 1:
            if coefficient > 0:
                if first:
                    simbol = ''
                else:
                    simbol = ' + 1'
            else:
                if first:
                    simbol = '-'
                else:
                    simbol = ' - 1'
        else:
            if first:
                simbol = str(coefficient)
            else:
                if coefficient > 0:
                    simbol = ' + ' + str(coefficient)
                else:
                    simbol = ' - ' + str(abs(coefficient))
        if i >= 1:
            simbol += 'x'
        if i >= 2:
            temp = str(i)
            for char in temp:
                simbol += str(degree[char])
            
        result += simbol
        first=False
    result += ' = 0'
    return result

k = int(input('Введите степень: '))
with open('task4_out.txt', 'w', encoding='utf-8') as file:
    file.write(polynom_gen(k))
print('Результат в файле task4_out.txt')