# Найдётся всё

# Поиск информации — одна из основных нужд в современном мире.
# Создайте программу, которая реализует маленький компонент поисковой системы.

# Формат ввода
# Вводится натуральное число N — количество страниц, среди которых требуется
# произвести поиск. В каждой из последующих N строк записаны заголовки страниц.
# В последней строке записан поисковый запрос.

# Формат вывода
# Вывести все заголовки страниц, в которых присутствует поисковый запрос
# (регистр не имеет значения). Порядок заголовков должен сохраниться.


strings = []
for count in range(int(input())):
    strings.append(input())

search = input().lower()

for string in strings:
    if string.lower().find(search) >= 0:
        print(string)
