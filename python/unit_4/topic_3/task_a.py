# Рекурсивный сумматор
#
# Большинство задач этой главы ориентировано на отработку навыков
# по разработке рекурсивных функций.
#
# Ваше решение будет использоваться как библиотека.
#
# Напишите функцию recursive_sum, которая находит сумму всех
# позиционных аргументов.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за
# исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не
# учитывается и показана для примера.

def recursive_sum(*args):
    if not args:
        return 0
    n, *args = args
    return n + recursive_sum(*args)


# print(recursive_sum(7, 1, 3, 2, 10))
