# Дайте чего-нибудь новенького!

# Главный повар детского сада хочет приготовить в праздничный день блюда,
# которые ни разу не готовил на этой неделе. В его распоряжении есть список
# блюд:
#     которые можно приготовить в столовой сегодня;
#     которые были приготовлены в каждый из дней недели.

# Формат ввода
# Число блюд (N), которые можно приготовить в столовой.
# N строк с названиями блюд. Число дней (M), о которых имеется информация.
# M блоков строк для каждого из списков. В первой строке каждого блока
# записано число блюд в заданный день, затем перечисляются эти блюда.

# Формат вывода
# Список блюд, которые ещё не готовились на этой неделе в алфавитном
# порядке. Если все возможные блюда уже были приготовлены, следует вывести
# «Готовить нечего».


dishes_next = []
for _ in range(int(input())):
    dishes_next.append(input())

dishes_prev = set()
for _ in range(int(input())):
    for _ in range(int(input())):
        dishes_prev.add(input())

dishes_left = False
for dish in sorted(dishes_next):
    if dish not in dishes_prev:
        print(dish)
        dishes_left = True

if not dishes_left:
    print('Готовить нечего')
