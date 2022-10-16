#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    if n < 0:
        if n in (-1, -2):
            return -1
        return fibonacci(n + 2) + fibonacci(n + 1)
    elif n == 0:
        return 0
    else:
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

list_result = []
number = int(input('Введите число: '))

for i in range(-number, number + 1):
    list_result.append(fibonacci(i))

print(list_result)