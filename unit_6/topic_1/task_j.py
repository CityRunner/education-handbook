"""
Лесенка

Напишите функцию stairs, принимающую вектор и возвращающую матрицу, в которой каждая строка является копией вектора со смещением.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример 1
    Ввод
        print(stairs(np.arange(3)))

    Вывод
        [[0 1 2]
        [2 0 1]
        [1 2 0]]

Пример 2
    Ввод
        print(stairs(np.arange(5)))

    Вывод
        [[0 1 2 3 4]
        [4 0 1 2 3]
        [3 4 0 1 2]
        [2 3 4 0 1]
        [1 2 3 4 0]]
"""

import numpy as np


def stairs(vector):
    size = len(vector)
    matrix = np.zeros((size, size), dtype="int32")
    for i in range(size):
        matrix[i] = np.roll(vector, i)
    return matrix
