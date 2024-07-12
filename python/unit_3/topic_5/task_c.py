# Без комментариев 2.0

# Как вы помните, когда вы комментируете свой код, перед его выполнением
# интерпретатор удаляет комментарии. Напишите программу, которая
# выполняет данную функцию за интерпретатор.

# Формат ввода
# Вводятся строки программы.

# Формат вывода
# Каждую строку нужно очистить от комментариев.
# А если комментарий — вся строка, то выводить её не нужно.

from sys import stdin

for line in stdin:
    if not line.startswith('#'):
        print(line.split('#')[0].rstrip('\n'))
