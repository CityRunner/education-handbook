# Потоковый НОД

# Напишите программу, находящую наибольшие общие делители для всех
# переданных в стандартный поток последовательностей чисел.

# Формат ввода
# Вводятся строки чисел, разделённых пробелами.

# Формат вывода
# Последовательность чисел — наибольшие общие делители всех
# последовательностей.

from sys import stdin
from math import gcd

gcd_list = []
for line in stdin:
    sequences = map(int, line.rstrip('\n').split())
    gcd_list.append(gcd(*sequences))
print('\n'.join(str(number) for number in gcd_list))
