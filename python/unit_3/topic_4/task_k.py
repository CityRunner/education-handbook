# Числовой прямоугольник 3.0

# Ребята в детском саду вновь учатся считать, и воспитательница решила
# сделать так, чтобы им было проще освоить новый навык. Для этого она
# хочет оформить список изучаемых чисел особым образом.
# Дети справляются весьма быстро, поэтому ей требуется программа,
# которая способна строить числовые прямоугольники. Напишите программу,
# которая строит числовой прямоугольник требуемого размера.

# Формат ввода
# В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.

# Формат вывода
# Нужно вывести сформированный числовой прямоугольник требуемого
# размера. Чтобы прямоугольник был красивым, каждый его столбец должен
# быть одинаковой ширины.

# Примечание
# itertools.product прекрасно подходит, чтобы избавиться от вложенных
# циклов.

from itertools import product, islice

height, width = int(input()), int(input())
length = len(str(height * width))
line = list()

for h, w in product(range(1, height + 1), range(1, width + 1)):
    line.append(str(((h - 1) * width + w)).rjust(length))
    if w == width:
        print(*line)
        line.clear()
