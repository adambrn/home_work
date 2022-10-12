#Реализуйте алгоритм перемешивания списка.
import random
list_num = [12, 5, 664, 63, 5, 73, 93, 127, 432, 64, 34]

#list_shuffled = list_num[:]
#random.shuffle(list_shuffled)

list_shuffled = []
list_tmp = list_num[:]
while  list_tmp != []:
            tmp = random.choice(list_tmp)
            list_tmp.remove(tmp)
            list_shuffled.append(tmp)

print(list_shuffled)