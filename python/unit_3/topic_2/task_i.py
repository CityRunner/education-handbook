# Зайка — 9

# Поможем детям подсчитать, сколько за окном поезда встречается животных и
# деревьев каждого вида.

# Формат ввода
# В каждой строке записано описание придорожной местности.
# Конец ввода обозначается пустой строкой.

# Формат вывода
# Список увиденного и их количество. Порядок вывода не имеет значения.


road_things = {}
while (roadside := input()) != '':
    for thing in roadside.split():
        if thing not in road_things:
            road_things[thing] = 1
        else:
            road_things[thing] += 1

for thing in road_things:
    print(f'{thing} {road_things[thing]}')
