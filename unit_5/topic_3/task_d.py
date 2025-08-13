"""
Контроль параметров

Напишите функцию only_positive_even_sum, которая принимает два параметра и возвращает их сумму.

Если один из параметров не является целым числом, то следует вызвать исключение TypeError. Если один из параметров не является положительным чётным числом, то следует вызвать исключение ValueError.

Примечание

Ваше решение должно содержать только функции. В решении не должно быть вызовов требуемых функций.

Пример 1
    Ввод:
        print(only_positive_even_sum("3", 2.5))

    Вывод:
        Вызвано исключение TypeError

Пример 2
    Ввод:
        print(only_positive_even_sum(-5, 4))

    Вывод:
        Вызвано исключение ValueError
"""

def only_positive_even_sum(a, b):
    if not all(type(x) is int for x in (a, b)):
        raise TypeError
    elif not all(x > 0 and x % 2 == 0 for x in (a, b)):
        raise ValueError
    return a + b
