# Числовой прямоугольник

# Ребята в детском саду учатся считать, и чтобы им было интереснее,
# воспитательница решила оформить список изучаемых чисел особым образом.
# Дети справляются весьма быстро, поэтому ей требуется программа способная
# строить числовые прямоугольники. Напишите программу, которая строит
# числовой прямоугольник требуемого размера.

# Формат ввода
# В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.

# Формат вывода
# Нужно вывести сформированный числовой прямоугольник требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец должен быть одинаковой
# ширины.


number = int()
height, width = int(input()), int(input())

for row in range(height):
    output = ''
    for col in range(1, width + 1):
        number += 1
        output += str(number).rjust(len(str(height * width))) + ' '
    print(output)
