# Шахматный «обед»

# Напишите функцию can_eat, которая принимает положение
# коня и другой фигуры в виде кортежей из двух координат,
# а возвращает булево значение: True если конь съедает
# фигуру и False иначе.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def can_eat(start, end):
    from itertools import product, chain
    ways = list(product((-1, 1), (-2, 2))) + list(product((-2, 2), (-1, 1)))
    for way in ways:
        destination = tuple(a + b for a, b in zip(start, way))
        if destination == end:
            return True
    return False


# result = can_eat((2, 1), (4, 2))
# print(result)
