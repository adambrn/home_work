#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input('Введите десятичное число: '))
bin_number = ''
if number == 0:
    bin_number = 0
while number > 0:
    bin_number = str(number % 2) + bin_number
    number //= 2
print('Ответ:', bin_number)