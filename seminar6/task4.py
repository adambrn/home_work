#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
s = input('Введите текст: ').split()
result = [word for word in s if 'абв' not in word]
print(*result)