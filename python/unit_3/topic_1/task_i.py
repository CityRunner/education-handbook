# Без комментариев

# Мы надеемся, вы пишите комментарии к своему коду. Если так, то интерпретатор
# удаляет их перед тем, как выполнить код. Напишите программу, которая выполняет
# данную функцию за интерпретатор.

# Формат ввода
# Вводятся строки программы.
# Признаком остановки является пустая строка.

# Формат вывода
# Каждую строку нужно очистить от комментариев.
# А если комментарий — вся строка, то выводить её не надо.


strings = []
while (string := input()) != '':
    strings.append(string)

for string in strings:
    stripped_string = ''
    comment_pos = string.find('# ')
    if comment_pos == -1:
        print(string)
    elif comment_pos == 0:
        continue
    else:
        print(string[:comment_pos].rstrip())