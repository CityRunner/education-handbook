# Числовая змейка 3.0

# Когда-то вы помогали детсадовцам с различными змейками. Давайте
# реализуем её на основе массивов.
# Напишите функцию snake, которая принимает ширину (M) и высоту (N)
# змейки, а также именованный параметр direction.

# Параметр direction могут принимать значения:
#     H — горизонтальная змейка, используется по умолчанию;
#     V — вертикальная змейка.

# Функция должна вернуть матрицу, представляющую змейку, с ячейками типа int16.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import numpy as np


def snake(M, N, direction='H'):
    sequence = np.arange(1, M * N + 1, dtype='int16')

    if direction == 'H':
        matrix = sequence.reshape(N, M)
        for i in range(N):
            if i % 2:
                matrix[i, :] = matrix[i, ::-1]
        return matrix
    else:
        matrix = sequence.reshape(M, N).transpose()
        for i in range(M):
            if i % 2:
                matrix[:, i] = matrix[::-1, i]
        return matrix
