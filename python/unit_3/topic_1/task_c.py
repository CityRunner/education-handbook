# Анонс новости

# Местная новостная компания заказала сайт. Его неотъемлемая часть — новостная
# лента. Чтобы пользователи могли быстрее анализировать статьи, нужно сократить
# заголовки. Напишите программу, которая сокращает длинные заголовки до
# требуемой длины и завершает их многоточием ... при необходимости.

# Формат ввода
# Вводится натуральное число L — необходимая длина заголовка.
# Вводится натуральное число N — количество заголовков, которые требуется
# сократить.
# В каждой из последующих N строк записано по одному заголовку.

# Формат вывода
# Сокращённые заголовки.

# Примечание
# Многоточие учитывается при подсчёте длины заголовка.


length = int(input())
headers = []

for count in range(int(input())):
    headers.append(input())

for header in headers:
    string = ''

    if len(header) <= length:
        letters = len(header)
        end = ''
    else:
        letters = length - 3
        end = '...'

    for letter in range(letters):
        string += header[letter]
    print(string + end)