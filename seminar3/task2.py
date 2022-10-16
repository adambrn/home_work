#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import sample
list_work = sample(range(10), 7)
print('Исходный список: ',list_work)
list_final = []
for i in range(len(list_work) // 2):
    list_final.append(list_work[i] * list_work[len(list_work) - 1 - i])
if (len(list_work) % 2 ):
        list_final.append(list_work[(len(list_work) // 2)] ** 2)
print('Результат: ',list_final)
