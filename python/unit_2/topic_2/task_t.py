# Зайка — 2
#
# По пути домой родители вновь решили сыграть с детьми в поиск зверушек.
#
# Формат ввода
# Три строки описывающих придорожную местность.
#
# Формат вывода
# Строка в которой есть зайка, а затем её длина.
# Если таких строк несколько, выбрать ту, что меньше всех лексикографически.

strings = []
bunny_strings = []

for index in range(3):
    strings.append(input())

for string in strings:
    if "зайка" in string:
        bunny_strings.append(string)

if bunny_strings:
    print(min(bunny_strings), len(min(bunny_strings)))
