#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform
list_work = [round(uniform(0,10),2) for _ in range(5)]
print('Исходный список: ',list_work)
result = abs(round(max(list_work) % 1 - min(list_work) % 1, 2))
print('Ответ :', result)