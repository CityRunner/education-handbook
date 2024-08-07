# Циклический генератор
#
# Напишите генератор cycle, который принимает список и работает
# аналогично итератору itertools.cycle.
#
# Примечание
#
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def cycle(ls: list):
    count = 0
    while True:
        if count >= len(ls):
            count = 0
        yield ls[count]
        count += 1


# print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
