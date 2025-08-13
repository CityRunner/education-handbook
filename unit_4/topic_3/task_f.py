"""
Сортировка слиянием

Мы уже реализовывали функцию merge, которая способна "слить" два отсортированных списка в один.
Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.

Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.

Примечание:
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана для примера.

Пример 1:
    Ввод:
        result = merge_sort([3, 2, 1])

    Вывод:
        # Вызов merge_sort([3, 2, 1])
        # Вызов merge_sort([3])
        # Вызов merge_sort([2, 1])
        # Вызов merge_sort([2])
        # Вызов merge_sort([1])
        result = [1, 2, 3]

Пример 2:
    Ввод:
        result = merge_sort([3, 1, 5, 3])

    Вывод:
        # Вызов merge_sort([3, 1, 5, 3])
        # Вызов merge_sort([3, 1])
        # Вызов merge_sort([3])
        # Вызов merge_sort([1])
        # Вызов merge_sort([5, 3])
        # Вызов merge_sort([5])
        # Вызов merge_sort([3])
        result = [1, 3, 3, 5]
"""

def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    list_l = merge_sort(unsorted_list[:mid])
    list_r = merge_sort(unsorted_list[mid:])
    return merge(list_l, list_r)


def merge(list_l, list_r):
    merge_sorted = list()
    while list_l and list_r:
        if list_l[0] < list_r[0]:
            merge_sorted.append(list_l.pop(0))
        else:
            merge_sorted.append(list_r.pop(0))
    while list_l:
        merge_sorted.append(list_l.pop(0))
    while list_r:
        merge_sorted.append(list_r.pop(0))
    return merge_sorted
