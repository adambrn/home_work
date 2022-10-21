#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if not number % 2:
        return False
    for i in range(3, int(number ** 0.5 + 1),2):
        if not number % i:
            return False
    return True

n = int(input('Введите целое число: '))
divisors_list = []
for i in range(1,  int(n ** 0.5 + 1)) :
    if n % i == 0: 
        if is_prime(i):
            divisors_list.append(i)
        if is_prime(n // i):
            divisors_list.append(n // i)
if not len(divisors_list):
    print('Число простое')
else:
    divisors_list.sort()
    print(*divisors_list)