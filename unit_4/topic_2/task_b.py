"""
Генератор матриц

Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.

Параметры функции:

    size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
    value — значение элементов списка (по-умолчанию 0).

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример 1:
    Ввод:
        result = make_matrix(3)
    Вывод:
        result = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

Пример 2:
    Ввод:
        result = make_matrix((4, 2), 1)
    Вывод:
        result = [
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
"""

from itertools import repeat


def make_matrix(size, value=0):
    if type(size).__name__ == 'int':
        width = height = size
    else:
        width, height = size
    return [list(repeat(value, width)) for _ in range(height)]
