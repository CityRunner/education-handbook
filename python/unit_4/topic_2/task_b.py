# Генератор матриц

# Напишите функцию make_matrix, которая создаёт, заполняет и
# возвращает матрицу заданного размера.
# Параметры функции:
#     size — кортеж (ширина, высота) или одно число (для
#     создания квадратной матрицы);
#     value — значение элементов списка (по-умолчанию 0).

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def make_matrix(size, value=0):
    from itertools import repeat
    if type(size).__name__ == 'int':
        width = height = size
    else:
        width, height = size
    return [list(repeat(value, width)) for _ in range(height)]


# result = make_matrix(3)
# print(result)
# result = make_matrix((4, 2), 1)
# print(result)
