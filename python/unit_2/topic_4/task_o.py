# Числовая змейка 2.0

# Воспитательнице вновь нужна программа, которая будет генерировать змейку из
# чисел. Напишите программу, которая строит числовую змейку требуемого размера.

# Формат ввода
# В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.

# Формат вывода
# Нужно вывести сформированную числовую змейку требуемого размера. Чтобы
# прямоугольник был красивым, каждый его столбец следует сделать одинаковой
# ширины.


matrix = []

height, width = int(input()), int(input())

for row in range(height):
    matrix += [[0] * width]

number = 1

for col in range(width):
    if col % 2 == 0:
        for row in range(height):
            matrix[row][col] = number
            number += 1
    else:
        for row in range(height - 1, -1, -1):
            matrix[row][col] = number
            number += 1

for row in range(height):
    output = ''
    for col in range(width):
        output += str(matrix[row][col]).rjust(len(str(height * width))) + ' '
    print(output)
