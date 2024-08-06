# Сортировка слиянием

# Мы уже реализовывали функцию merge, которая способна "слить" два
# отсортированных списка в один. Чаще всего её применяют в рекурсивном
# алгоритме сортировки слиянием.
# Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением
# рекурсивных. Трассировка вызова рекурсивной функции в обработке ответа
# не учитывается и показана для примера.


def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    left = merge_sort(unsorted_list[:mid])
    right = merge_sort(unsorted_list[mid:])
    return merge(left, right)


def merge(left, right):
    merge_sorted = list()
    while left and right:
        if left[0] < right[0]:
            merge_sorted.append(left.pop(0))
        else:
            merge_sorted.append(right.pop(0))
    while left:
        merge_sorted.append(left.pop(0))
    while right:
        merge_sorted.append(right.pop(0))
    return merge_sorted


# print(merge_sort([8, 3, 1, 5, 0, 2, 9, 4]))
# print(merge_sort([3, 2, 1]))
# print(merge_sort([3, 1, 5, 3]))
