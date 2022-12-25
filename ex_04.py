# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

print('Введите десятичное число: ')
n = int(input())
str_dv = ''
if n < 2:
    print(n)
else:
    while n >= 2:
        str_dv = str_dv + (str(n % 2))
        n = n // 2
    str_dv = str_dv + (str(n))
    # print(str_dv)
    str_convert= ''.join(reversed(str_dv))
    print(str_convert)