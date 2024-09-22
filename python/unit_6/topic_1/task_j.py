# Лесенка

# Напишите функцию stairs, принимающую вектор и возвращающую матрицу,
# в которой каждая строка является копией вектора со смещением.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import numpy as np


def stairs(vector):
    size = len(vector)
    matrix = np.zeros((size, size), dtype="int32")
    for i in range(size):
        matrix[i] = np.roll(vector, i)
    return matrix
