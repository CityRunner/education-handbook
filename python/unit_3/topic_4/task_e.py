# Список покупок

# Поход в магазин часто вызывает проблемы. Если не подготовить
# список, можно уйти в магазин за хлебом, а вернуться с десятком
# пакетов. Напишите программу, которая собирает пожелания семьи
# (мамы, папы и дочки) в единый список.

# Формат ввода
# В трёх строках записаны желаемые продукты (через запятую и пробел).

# Формат вывода
# Отсортированный по алфавиту список продуктов с нумерацией.

# Примечание
# Помните, что итераторы можно применять к другим итераторам.

from itertools import chain

values = sorted(list(chain(input().split(', '),
                           input().split(', '),
                           input().split(', '))))
for index, value in enumerate(values, 1):
    print(f'{index}. {value}')
