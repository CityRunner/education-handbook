# Матрица умножения
#
# Напишите функцию multiplication_matrix, которая принимает размер
# матрицы (N) и возвращает массив, описывающий таблицу умножения N на N.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import numpy as np


def multiplication_matrix(size):
    matrix = np.arange(1, size + 1)
    return matrix * matrix.reshape(size, 1)
