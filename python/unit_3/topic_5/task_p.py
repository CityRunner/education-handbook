# Найдётся всё 3.0
# Давайте вновь напишем небольшой компонент поисковой системы.

# Формат ввода
# Сначала вводится поисковый запрос. Затем вводятся имена файлов,
# среди которых следует произвести поиск.

# Формат вывода
# Выведите все имена файлов, в которых есть поисковая строка без учета
# регистра и повторяющихся пробельных символов. Если ни в одном файле
# информация не была найдена, выведите "404. Not Found".

# Примечание
# Система поиска должна обрабатывать строки "a&nbsp;&nbsp;&nbsp;&nbsp;b",
# "a b" и "a\nb" как одинаковые.

from sys import stdin
import json

search = input().replace('&nbsp;', ' ').replace('\n', ' ').lower()
found_in = []

for file_name in stdin.readlines():
    with open(file_name := file_name.strip('\n'), encoding='UTF-8') as file_in:
        data = file_in.read().replace('&nbsp;', ' ').replace('\n', ' ').lower()
        while '  ' in data:
            data = data.replace('  ', ' ')
        if search in data:
            found_in.append(file_name)

if found_in:
    print('\n'.join(name for name in found_in))
else:
    print('404. Not Found')
