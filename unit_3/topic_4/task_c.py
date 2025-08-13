"""
Рациональная считалочка

Напишите программу, которая производит счёт по заданным параметрам.

Формат ввода:
    В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.

Формат вывода:
    Последовательность чисел с заданными параметрами.

Example 1:
    Input:
        3.2 6.4 0.8
    Output:
        3.20
        4.00
        4.80
        5.60
        6.40

Example 2:
    Input:
        3.14 10 1.57
    Output:
        3.14
        4.71
        6.28
        7.85
        9.42
"""

from itertools import count

start, stop, step = map(float, input().split())
for value in count(start, step):
    if value > stop:
        break
    else:
        print(round(value, 2))
