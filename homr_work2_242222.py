# Задача 14
# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# some_str = input('Введите вещественное число: ')

# if '.' in some_str:
# 	some_str = some_str.replace('.', '')

# if '-' in some_str:
# 	some_str = some_str.replace('-', '')

# summ = 0
# for i in range(len(some_str)):
#     summ += int(some_str[i])
# print(summ)

#=============================================================

# Задача 15
# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n_str = input('Введите любое целое число ')
# if '.' in n_str or '-' in n_str or ',' in n_str:
#     print('Вы ввели некорректное число')
#     exit()
# n = int(n_str)

# rez_str = [0] * n

# composition_n = 1

# for i in range(n):
#     composition_n = composition_n * (i + 1)
#     rez_str[i] = composition_n

# print(rez_str)

#=======================================================================

# Задача 16
# Задайте список из n чисел последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n_str = input('Введите любое целое число ')
# if '.' in n_str or '-' in n_str or ',' in n_str:
#     print('Вы ввели некорректное число')
#     exit()
# n = int(n_str)

# rez_str = [0] * n

# for i in range(n):
#     rez_str[i] = round((1 + 1 / (i+1)) ** (i+1), 2)
# print(rez_str)

#=======================================================================
# 
# 
# Задача 18
# Реализуйте алгоритм перемешивания списка.
# Попробовал сам сваять алгоритм...

in_list = list(input('Напишите любую строку, которая будет изображать роль СПИСКА: '))
print(in_list)
n = len(in_list)
out_list = [0] * n
from random import randint
for i in range(n):
    index = randint(0, n - 1)
    print(index)
    out_list[i] = in_list[index]
    in_list.remove(in_list[index])
    n = n -1

print(out_list)

