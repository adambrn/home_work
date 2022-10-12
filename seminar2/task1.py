#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input('Введите число :')
summ = 0
for digit in number:
    if digit.isdigit():
        summ += int(digit)
print('Сумма цифр', summ)