# Анонс новости 2.0

# Попробуем ещё раз сократить заголовки для статей в ленте новостного сайта.
# Давайте сделаем программу, которая сокращает длинный заголовок до требуемой
# длины и завершает его многоточием ..., если это требуется.

# Формат ввода
# Вводится натуральное число L — необходимая длина заголовка.
# Вводится натуральное число N — количество строк в заголовке новости.
# В каждой из последующих N строк записано по одной строке заголовка.

# Формат вывода
# Сокращённый заголовок.

# Примечание
# Многоточие учитывается при подсчёте длины заголовка.
# Символ перевода строки при подсчёте длины не учитывается.


header = []
max_length = int(input())
for _ in range(int(input())):
    header.append(input())

length = len(''.join(header))
header_line = '\n'.join(header)

if length <= max_length:
    print(header_line)
else:
    new_header = ''
    count = 0
    for symbol in header_line:
        new_header += symbol
        if symbol != '\n':
            count += 1
        if count == max_length - 3:
            break
    print(new_header + '...')
