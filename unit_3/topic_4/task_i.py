"""
Таблица умножения 3.0

Местная фабрика канцелярских товаров заказала программу, которая генерирует таблицы умножения.
Давайте поможем производителю.

Формат ввода:
    Вводится одно натуральное число — требуемый размер таблицы.

Формат вывода:
    Таблица умножения заданного размера.

Примечание:
    itertools.product отличный способ, чтобы избавиться от вложенных циклов.

Example 1:
    Input:
        3
    Output:
        1 2 3
        2 4 6
        3 6 9

Example 2:
    Input:
        5
    Output:
        1 2 3 4 5
        2 4 6 8 10
        3 6 9 12 15
        4 8 12 16 20
        5 10 15 20 25
"""

from itertools import product, islice

size = int(input())
numbers = list(range(1, size + 1))
table = [str(a * b) for a, b in product(numbers, numbers)]
for row in range(size):
    print(' '.join(islice(table, row * size, (row + 1) * size)))
