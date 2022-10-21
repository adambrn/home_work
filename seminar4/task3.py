#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности.

sequence = input('Введите последовательность цифр: ')
unique_list =[]
for digit in sequence:
    if sequence.count(digit) == 1:
        unique_list.append(digit)
if not len(unique_list):
    print('Нет неповторяющихся цифр')
else:
    print(*unique_list)