# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
j = 0
flag = -1
while (j < len(list)):
    if list[j] % 1 != 0:
        flag = j
        j = len(list)
    j = j+1
if (flag == -1):
    print('В списке значений нет вещественных чисел')
else: 
    minn= list[flag] % 1
    i_minn = flag
    maxn = list[flag] % 1
    i_maxn = flag
    for i in range(len(list)):
        temp = list[i] % 1
        if temp != 0:
            if minn > temp:
                minn = temp
                i_minn = i
            if maxn < temp:
                maxn = temp
                i_maxn = i
    print(minn)
    print(maxn)
    raznost = list[i_maxn] % 1 - list[i_minn] % 1
    print(raznost)