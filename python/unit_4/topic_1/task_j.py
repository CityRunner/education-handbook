"""
Полное решение

Слияние

Напишите функцию merge, которая принимает два отсортированных по возрастанию кортежа целых чисел, а возвращает один из всех переданных чисел.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.
    В этой задаче отключены стандартные сортировки.

Пример 1:
    Ввод:
        result = merge((1, 2), (3, 4, 5))
    Вывод:
        result = (1, 2, 3, 4, 5)

Пример 2:
    Ввод:
        result = merge((7, 12), (1, 9, 50))
    Вывод:
        result = (1, 7, 9, 12, 50)
"""

def merge(tuple_1, tuple_2):
    list_1 = list(tuple_1)
    list_2 = list(tuple_2)
    result = []
    while list_1 and list_2:
        if list_1[0] > list_2[0]:
            result.append(list_2.pop(0))
        else:
            result.append(list_1.pop(0))
    result.extend(list_1 + list_2)
    return tuple(result)
