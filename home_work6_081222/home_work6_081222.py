# Задача 5
# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние
# по числовому ряду числа в диапазоны.

# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

# some_list = list(map(int, input("Введите числа через ',': ").split(',')))
# some_list.sort()
# #print(some_list)

# out_list1 = [[some_list[0]]]
# first_member = some_list[0]


# for i in some_list[1:]:
#     if i-first_member == 1:
#             out_list1[-1].append(i)
#     else:
#             out_list1.append([i])
#     first_member = i
# first = [i[0] for i in out_list1]
# last = [i[len(i)-1] for i in out_list1]

# for i in range(len(first)):
#     if first[i] != last[i]:
#         print(f'{first[i]} - {last[i]}')
        
#     else:
#         print(first[i])

# надо доработать вывод результата
# ==========================================================

# Задача 6
# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения :
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений


with open('file_in.txt', 'w+') as data:
    data.write('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
    string = data.readline()
    

def rle_compress(string):
    compress_string = ''
    count = 1
    char = string[0]
    for i in range(1, len(string)):
        if string[i] == char:
            count += 1
        else:
            compress_string = compress_string  + char + str(count)
            char = string[i]
            count = 1
    compress_string = compress_string + str(count)
    compress_string = compress_string.replace('1', '')
    return compress_string


def rle_decompress(string):
    decompress_string = ''
    factors = 0
    for i in range(len(string) - 1):
        if string[i].isdigit():
            factors += int(string[i])
        else:
            decompress_string += string[i] * factors
        factors = 0

    return decompress_string


with open('file_in.txt', 'r') as file:
    decompress_string = file.read()
if decompress_string == '':
        print('Вы ввели пустую строку')
        exit()    

with open('file_out.txt', 'w') as file:
    compress_string = rle_compress(decompress_string)
    file.write(compress_string)

print('Строка несжатых данных: ' + decompress_string)
print('Строка сжатых данных: ' + rle_compress(decompress_string))

# В решении использовал задачу из прошлого ДЗ, скорее всего можно сократить 
# алгоритм, так как тас не просят проводить декомпрессию
