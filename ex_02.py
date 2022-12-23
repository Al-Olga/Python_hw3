# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
list = []
multi = []
print('Введите количество элементов: ')
n = int(input())
for _ in range(n):
    list.append(random.randint(0, 10))
print(list)
i=0
while i < ( n / 2):
    multi.append(list[i]*list[n-1-i])
    i = i + 1
print(multi)
