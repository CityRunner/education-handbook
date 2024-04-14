# Это будет шедевр!

# Главный повар детского сада хочет быстрее выбирать блюда для готовки.
# В его распоряжении есть список продуктов, а также набор блюд.
# Напишите программу, способную быстро определить блюда, которые можно
# приготовить.

# Формат ввода
# Число продуктов (N), которые имеются в наличии.
# N строк с названиями продуктов.
# Число рецептов (M), о которых имеется информация.
# M блоков строк для каждого из рецептов.
# В первой строке каждого блока записано название блюда.
# Во второй — число ингредиентов.
# Затем перечисляются сами ингредиенты, требуемые для приготовления блюда.

# Формат вывода
# Список блюд, которые можно приготовить в алфавитном порядке.
# Если ни одно из блюд нельзя приготовить, следует вывести «Готовить нечего».


ingredients_avail = []
for _ in range(int(input())):
    ingredients_avail.append(input())

recipes = {}
for _ in range(int(input())):
    name = input()
    recipes[name] = []
    for _ in range(int(input())):
        recipes[name].append(input())

dishes_avail = []
for dish in recipes:
    available = True
    for ingredient in recipes[dish]:
        if ingredient not in ingredients_avail:
            available = False
    if available:
        dishes_avail.append(dish)


if len(dishes_avail) == 0:
    print('Готовить нечего')
else:
    for dish in sorted(dishes_avail):
        print(dish)
