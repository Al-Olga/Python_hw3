# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

print('Введите десятичное число: ')
n = int(input())
if n < 2:
    print(n)
else:
    list = []
    while n >= 2:
        list.append(str(n % 2))
        n = n // 2
    list.append(str(n))
    print(list)