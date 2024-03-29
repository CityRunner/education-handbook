# Корень зла

# Не все любят математику, а кто-то даже считает её настоящим злом во плоти,
# хотя от неё никуда не деться. К примеру, Python изначально разрабатывался
# только для решения математических задач, поэтому давайте используем его,
# чтобы найти корни уравнения.

# Формат ввода
# Вводится 3 вещественных числа aa, bb, cc — коэффициенты уравнения вида:
# ax2+bx+c=0ax2+bx+c=0.

# Формат вывода
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке
# возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».

# Примечание
# Обратите внимание, что ограничения на значения коэффициентов отсутствуют.


a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = round((- c / b), 2)
        print(x)
else:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = round((- b + D ** (1 / 2)) / (2 * a), 2)
        x2 = round((- b - D ** (1 / 2)) / (2 * a), 2)
        if x1 < x2:
            print(x1, x2)
        else:
            print(x2, x1)
    elif D == 0:
        x = round(- b / (2 * a), 2)
        print(x)
    else:
        print("No solution")
