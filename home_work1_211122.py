# Задача 6
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Вариант 1:
#======
# n = int(input())
# if n == 6 or n == 7:
#         print('да')
# else:
#         print('нет')



# Вариант 2:
#======
# some_str = '6, 7'
# n = input()
# if n in some_str:
#     print('да')
# else:
#     print('нет')

#===================================================================

# Задача 7
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))

#====================================================================

# Задача 8
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координаты X: '))
# y = int(input('Введите координаты Y: '))
# if x == 0 and y == 0:
#     print('Точка лежит в начале координат')
# elif x == 0:
#     print('Точка лежит на оси Y')
# elif y == 0:
#     print('Точка лежит на оси X')
# elif x > 0 and y > 0:
#     print('Точка лежит в 1 четверти')
# elif x < 0 and y > 0:
#     print('Точка лежит в 2 четверти')
# elif x < 0 and y < 0:
#     print('Точка лежит в 3 четверти')
# else:
#     print('Точка лежит в 4 четверти')

#========================================================================

# Задача 9
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('Введите номер четверти: '))
# if n == 1:
#     print('Координаты точек лежат в диапазоне x > 0 и y > 0')
# elif n ==2:
#     print('Координаты точек лежат в диапазоне x < 0 и y > 0')
# elif n == 3:
#     print('Координаты точек лежат в диапазоне x < 0 и y < 0')
# elif n == 4:
#     print('Координаты точек лежат в диапазоне x > 0 и y < 0')
# else:
#     print('Вы ввели ошибочный номер четверти')

#=========================================================================

# Задача 10
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xya = input('Введите через запятую координаты точки A: ').split(',')
xyb = input('Введите через запятую координаты точки B: ').split(',')


line = ((int(xya[0]) - int(xyb[0])) ** 2 + (int(xya[1]) - int(xyb[1])) ** 2) ** (0.5)

print(line)

#end


