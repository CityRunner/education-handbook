# Список покупок 2.0

# Давайте вновь поможем человеку с покупками. Разработайте программу,
# которая собирает пожелания семьи в единый список.

# Формат ввода
# В первой строке задано натуральное число N — количество членов
# семьи. В следующих N строках записаны желаемые продукты (через
# запятую и пробел).

# Формат вывод
# Отсортированный по алфавиту список продуктов с нумерацией.

# Примечание
# Помните, что итераторы можно хранить в списке, а его можно распаковать
# в любую функцию.

from itertools import chain

items = chain.from_iterable(input().split(', ') for _ in range(int(input())))
for num, item in enumerate(sorted(list(items))):
    print(f"{num + 1}. {item}")