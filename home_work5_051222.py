# Задача 38
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input('Введите несколько произволных слов на кирилице: ')

# text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, text.split()))
# print(text_list)

#==========================================================================

# Задача 39
# Создайте программу для игры в ""Крестики-нолики"".
# Решение подсмотрел, но кое где подправил/сократил код

# board = list(range(1,10))


# def design_board(board):
#     print('-'*13)
#     for i in range(3):
#         print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*13)

# # design_board(board)

# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = int(input('Ваш ход, выберите ячейку ' + tic_tac + ' --> '))
   
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Еще раз попробуй')

# def victory_check(board):
#     victory = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False

# def game(board):
#     counter =0
#     vic = False
#     while not vic:
#         design_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             tt_win = victory_check(board)
#             if tt_win:
#                 print(tt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Победила, ДРУЖБА)')
#         design_board(board)
# game(board)


# Задача 40
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('file_in.txt', 'w+') as data:
#     data.write('AAAAAAAAABBCFFFFFDDOGGGGGGGGGGGGG')
#     string = data.readline()

# def rle_compress(string):
#     compress_string = ''
#     count = 1
#     char = string[0]
#     for i in range(1, len(string) - 1):
#         if string[i] == char:
#             count += 1
#         else:
#             compress_string = compress_string + str(count) + char
#             char = string[i]
#             count = 1
#     compress_string = compress_string + char
#     return compress_string


# def rle_decompress(string):
#     decompress_string = ''
#     factors = 0
#     for i in range(len(string) - 1):
#         if string[i].isdigit():
#             factors += int(string[i])
#         else:
#             decompress_string += string[i] * factors
#         factors = 0
# #    print(decompress_string)

#     return decompress_string


# with open('file_in.txt', 'r') as file:
#     decompress_string = file.read()

# with open('file_out.txt', 'w') as file:
#     compress_string = rle_compress(decompress_string)
#     file.write(compress_string)

# print('Строка несжатых данных: ' + decompress_string)
# print('Строка сжатых данных: ' + rle_compress(decompress_string))

