#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
number = int(input('Введите число : '))
multi = 1
dic = {}
for i in range(1,number+1):
    dic[i] = round((1+1/i) ** i,2)
print(dic)
print('Сумма: ',round(sum(dic.values()),2))