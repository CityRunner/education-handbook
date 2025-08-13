"""
Полное решение

Классная точка 3.0

Давайте расширим функционал класса, написанного вами в задаче «Классная точка 2.0».

Создайте класс PatchedPoint — наследника уже написанного вами Point.

Требуется реализовать следующие виды инициализации нового класса:

    параметров не передано — координаты точки равны 0;
    передан один параметр — кортеж с координатами точки;
    передано два параметра — координаты точки.

Примечание

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1:
    Ввод:
        point = PatchedPoint()
        print(point.x, point.y)
        point.move(2, -3)
        print(point.x, point.y)

    Вывод:
        0 0
        2 -3

Пример 2:
    Ввод:
        first_point = PatchedPoint((2, -7))
        second_point = PatchedPoint(7, 9)
        print(first_point.length(second_point))
        print(second_point.length(first_point))

    Вывод:
        16.76
        16.76
"""

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args
