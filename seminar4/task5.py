#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.
code = {
        '0': '\u2070',
        '1': '\u00B9',
        '2': '\u00B2',
        '3': '\u00B3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079'
            }
uncode = {v: k for k, v in code.items()}

def parse_polynom(p):
    tmp = {}
    for elem in [x for x in p.replace('-', '+-').replace('^','').split('+')]:
        if 'x' in elem:
            if elem.split('x')[0] == '':
                digit = 1
            else: digit = int(elem.split('x')[0])
            if elem.split('x')[1] == '':
                degree = 1
            else:
                if elem.split('x')[1] in uncode:
                    degree = int(uncode[elem.split('x')[1]])
                else: 
                    degree = int(elem.split('x')[1])
            tmp[degree] = digit    
        else:
            if elem != '':
                tmp[0] = int(elem)
    max_degree = int(max(tmp.keys()))
    coefficient_list = [0] * (max_degree + 1)
    for key,value in tmp.items():
         coefficient_list[key] = value
    return coefficient_list

def sum_polynom(p1,p2):
    result_list = [x+y for x,y in zip(p1,p2)] + (p1 if len(p1) >= len(p2) else p2)[min(len(p1), len(p2)):]
    return result_list

def polynom_gen(coefficient_list):
    first=True
    result=''
    for i in range(len(coefficient_list) - 1, -1, -1):
        coefficient = coefficient_list[i]
        if coefficient == 0:
            continue
        if abs(coefficient) == 1:
            if coefficient > 0:
                if first:
                    simbol = ''
                elif i == 0:
                    simbol = ' + 1'
                else :
                    simbol = ' + '
            else:
                if first:
                    simbol = '-'
                elif i == 0:
                    simbol = ' - 1'
                else :
                    simbol = ' - '
        else:
            if first:
                simbol = str(coefficient)
            else:
                if coefficient > 0:
                    simbol = ' + ' + str(coefficient)
                else:
                    simbol = ' - ' + str(abs(coefficient))
        if i >= 1:
            simbol += 'x'
        if i >= 2:
            temp = str(i)
            for char in temp:
                simbol += str(code[char])
            
        result += simbol
        first=False
    result += ' = 0'
    return result

with open('task5_in1.txt', 'r', encoding='utf-8') as file:
    polynom1 = file.readline().replace(' ','').rstrip('\n').split('=')[0]
with open('task5_in2.txt', 'r', encoding='utf-8') as file:
    polynom2 = file.readline().replace(' ','').rstrip('\n').split('=')[0]
result = polynom_gen(sum_polynom(parse_polynom(polynom2),parse_polynom(polynom1)))
with open('task5_out.txt', 'w', encoding='utf-8') as file:
    file.write(result)
print('Результат в файле task5_out.txt')
