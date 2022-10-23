# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data): 
    encode = "" 
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1
        encode += str(count) + data[i]
        i = i + 1
    return encode

def rle_decode(data): 
    decode = '' 
    tmp = '' 
    for char in data: 
        if char.isdigit(): 
            tmp += char 
        else: 
            decode += char * int(tmp) 
            tmp = '' 
    return decode
 
 
with open('task4_in_encode.txt', 'r', encoding='utf-8') as file:
    text = file.readline().rstrip('\n')

print('Строка из файла: ', text)
print('Кодированая строка: ', rle_encode(text))
print()

with open('task4_out_encode.txt', 'w', encoding='utf-8') as file:
    file.write(rle_encode(text))

with open('task4_in_decode.txt', 'r', encoding='utf-8') as file:
    text = file.readline().rstrip('\n')

print('Кодированая строка  из файла: ', text)
print('Декодированая строка: ', rle_decode(text))

with open('task4_out_decode.txt', 'w', encoding='utf-8') as file:
    file.write(rle_decode(text))
