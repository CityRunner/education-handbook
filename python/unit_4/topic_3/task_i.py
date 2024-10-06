"""
Циклический генератор

Напишите генератор cycle, который принимает список и работает аналогично итератору itertools.cycle.

Примечание:
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1:
    Ввод:
        print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))

    Вывод:
        1 2 3 1 2

Пример 2:
    Ввод:
        print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))

    Вывод:
        1 2 3 4 1 2 3 4 1 2 3 4 1 2 3
"""

def cycle(num_list):
    count = 0
    while True:
        if count >= len(num_list):
            count = 0
        yield num_list[count]
        count += 1
