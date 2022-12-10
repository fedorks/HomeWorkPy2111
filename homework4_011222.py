# Задача 30.
# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

# import math
# d = (input('Введите вещественное число 10**(-1) ≤ d ≤ 10**(-10): '))
# if ',' in d:
#     d = d.replace(',','.')
# if '.' in d:
#     ind = d.index('.')
# new_pi = round(math.pi, (len(d) - 1 - ind))
# print(new_pi)

#===============================================================

# Задача 31.
# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# n = int(input('Введите натуральное число: '))

# out_list = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             out_list.append(i)
# print(out_list)

#==================================================
# # Вариант 2
# n = int(input('Введите натуральное число: '))
# out_list = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         index = 1
#         for j in range(2, ( i // 2 + 1)):
#             if(i % j == 0):
#                 index = 0
#                 break
#         if(index == 1):
#             out_list.append(i)
# print(out_list)

#================================================

# Задача 32
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

n = int(input('Введите количество элементов последовательности: '))
from random import randint
numb = []
for i in range(n):
    numb.append(randint(0, 10))
print(numb)

out_numb = []
for i in range(len(numb)):
    if numb[i] not in out_numb:
        out_numb.append(numb[i])
    else:
        out_numb.remove(numb[i])
        numb.remove(numb[i])
print(numb)
print(out_numb)

