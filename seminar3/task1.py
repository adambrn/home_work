#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import sample
list_work = sample(range(100), 10)
print(list_work)
summ = 0
for i in range(1,len(list_work),2):
    summ += list_work[i]
print(summ)