# Частная собственность

# Ребята приносят игрушки в детский сад и играют все вместе. Сегодня они
# решили выяснить, игрушки какого типа принадлежат только одному из детей.
# Напишите программу, которая по списку детей и их игрушек определит
# «частную собственность».

# Формат ввода
# В первой строке задается количество детей в группе (N). В каждой из
# следующих N строк записано имя ребенка и его игрушки в формате: Имя:
# игрушка1, игрушка2, ....

# Формат вывода
# Список игрушек, которые есть только у одного из детей в алфавитном порядке.


kids_toys = {}
toys = set()
for _ in range(int(input())):
    inp = input().split(': ')
    this_kid_toys = inp[1].split(', ')
    toys = toys.union(set(this_kid_toys))
    kids_toys[inp[0]] = set(this_kid_toys)

private_toys = []
for toy in toys:
    owners = 0
    for kid in kids_toys:
        if toy in kids_toys[kid]:
            owners += 1
    if owners <= 1:
        private_toys.append(toy)

print('\n'.join(sorted(private_toys)))
