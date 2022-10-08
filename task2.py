#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

value = (True, False)
print('X'.ljust(6),'Y'.ljust(6),'Z'.ljust(6), '¬(X ⋁ Y ⋁ Z)'.ljust(15),'¬X ⋀ ¬Y ⋀ ¬Z'.ljust(15))
for x in value:
    for y in value:
        for z in value:
            print(str(x).ljust(6),str(y).ljust(6),str(z).ljust(6),
            str(not(x or y or z)).ljust(15),
            str((not x) and (not y) and (not z)).ljust(15), sep = '|')
