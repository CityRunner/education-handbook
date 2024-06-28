# Таблица умножения 3.0

# Местная фабрика канцелярских товаров заказала программу, которая
# генерирует таблицы умножения. Давайте поможем производителю.

# Формат ввода
# Вводится одно натуральное число — требуемый размер таблицы.

# Формат вывода
# Таблица умножения заданного размера.

# Примечание
# itertools.product отличный способ, чтобы избавиться от вложенных
# циклов.

from itertools import product, islice

size = int(input())
numbers = [num for num in range(1, size + 1)]
raw_table = [str(a * b) for a, b in product(numbers, numbers)]

for row in range(size):
    print(' '.join(islice(raw_table, row * size, (row + 1) * size)))
