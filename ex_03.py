# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:
# [7, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
j = 0
flag = 0
while (list[j] % 1 != 0) and (flag == 0):
    minn= list[0] % 1
    i_minn = 0
    maxn = list[0] % 1
    i_maxn = 0
    flag = 1
    j = j + 1
for i in range(len(list)):
    temp = list[i] % 1
    if temp != 0:
        if minn > temp:
            minn = temp
            i_minn = i
        if maxn < temp:
            maxn = temp
            i_maxn = i
raznost = list[i_maxn] % 1 - list[i_minn] % 1
print(raznost)