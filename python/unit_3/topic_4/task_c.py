# Рациональная считалочка

# Напишите программу, которая производит счёт по заданным параметрам.

# Формат ввода
# В одну строку через пробел вводятся 3 рациональных числа — начало
# счета, конец и шаг.

# Формат вывода
# Последовательность чисел с заданными параметрами.

from itertools import count

start, end, step = input().split()
for value in count(float(start), float(step)):
    if value <= float(end):
        print(round(value, 2))
    else:
        break
