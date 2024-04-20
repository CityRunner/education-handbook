# Зайка — 10

# Поможем детям разобраться, что именно они увидели рядом с зайками.

# Формат ввода
# В каждой строке записано описание придорожной местности.
# Конец ввода обозначается пустой строкой.

# Формат вывода
# Определите список увиденного рядом с зайками без повторений.
# Порядок вывода не имеет значения.

# Примечание
# Считается, что объект находится рядом, если он записан справа или слева от
# требуемого.


bunny = 'зайка'
neigbors = set()
while (inp := input()) != '':
    objs = inp.split()
    for pos, obj in enumerate(objs):
        if obj == bunny:
            if pos > 0:
                neigbors.add(objs[pos - 1])
            if pos < (len(objs) - 1):
                neigbors.add(objs[pos + 1])

print('\n'.join(neigbors))
