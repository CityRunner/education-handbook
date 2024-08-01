# В эфире рубрика «Эксперименты»

# Лаборанты проводят эксперимент и запросили разработку системы
# обработки данных. Результатами эксперимента должны стать пары
# рациональных чисел.

# Для работы им требуются функции:
#     enter_results(first, second, ...) — добавление данных одного или
#     нескольких результатов (гарантируется, что количество параметров
#     будет чётным);
#     get_sum() — возвращает пару сумм результатов экспериментов;
#     get_average() — возвращает пару средних арифметических значений
#     результатов экспериментов.
# Все вычисления производятся с точностью до сотых.

# Примечание
# В решении не должно быть вызовов требуемых функций.


def enter_results(*args):
    global results
    results += list(args)


def get_sum():
    odd_sum = round(sum(results[::2]), 2)
    evn_sum = round(sum(results[1::2]), 2)
    return odd_sum, evn_sum


def get_average():
    odd, evn = get_sum()
    length = len(results) / 2
    odd_average = round(odd / length, 2)
    evn_average = round(evn / length, 2)
    return odd_average, evn_average


results = list()


# enter_results(3.5, 2.14, 45.2, 37.99)
# print(get_sum(), get_average())
# enter_results(5.2, 7.3)
# print(get_sum(), get_average())
# enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
# print(get_sum(), get_average())
