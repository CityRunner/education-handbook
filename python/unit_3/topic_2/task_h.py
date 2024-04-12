# Кашееды — 4

# Каждый воспитанник детского сада любит одну или несколько каш.
# Поможем воспитателю составить список детей, которые любят конкретную кашу.

# Формат ввода
# В первой строке задаётся количество детей в группе (N). В следующих N строках
# записана фамилия ребенка и список его любимых каш. В последней строке
# записана каша, информацию о которой хочет получить воспитатель.

# Формат вывода
# Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».


eaters = {}
porridge_eaters = []
none = 'Таких нет'

for _ in range(int(input())):
    porridges = input().split()
    eaters[porridges.pop(0)] = porridges

porridge = input()
for name in eaters:
    if porridge in eaters[name]:
        porridge_eaters.append(name)

if len(porridge_eaters) > 0:
    for name in sorted(porridge_eaters):
        print(name)
else:
    print(none)
