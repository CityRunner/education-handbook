"""
Шахматный «обед»

Напишите функцию can_eat, которая принимает положение коня и другой фигуры в виде кортежей из двух координат, а возвращает булево значение: True если конь съедает фигуру и False иначе.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример 1:
    Ввод:
        result = can_eat((2, 1), (4, 2))
    Вывод:
        result = True

Пример 2:
    Ввод:
        result = can_eat((5, 5), (6, 6))
    Вывод:
        result = False
"""

from itertools import product, chain


def can_eat(start, end):
    ways = list(product((-1, 1), (-2, 2))) + list(product((-2, 2), (-1, 1)))
    for way in ways:
        destination = tuple(a + b for a, b in zip(start, way))
        if destination == end:
            return True
    return False
