#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
number = int(input('Введите число :'))
multi = 1
array = []
for i in range(number):
    multi *= i + 1
    array.append(multi)
print(array)