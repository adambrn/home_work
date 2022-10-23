#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
s = input('Введите текст').split()
for word in s:
    if 'абв' in word:
        s.remove(word)
print(*s)
