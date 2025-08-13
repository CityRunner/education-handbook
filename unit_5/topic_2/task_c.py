"""
Классная точка 5.0

Согласитесь, что использовать операторы куда удобнее, чем обыкновенные методы. Давайте вспомним о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.

При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной на заданное кортежем расстояние по осям x и y.
При выполнении кода point += (x, y) производится перемещение изначальной точки.

Напомним, что сейчас мы модернизируем только класс PatchedPoint.

Примечание

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1:
    Ввод:
        point = PatchedPoint()
        print(point)
        new_point = point + (2, -3)
        print(point, new_point, point is new_point)

    Вывод:
        (0, 0)
        (0, 0) (2, -3) False

Пример 2:
    Ввод:
        first_point = second_point = PatchedPoint((2, -7))
        first_point += (7, 3)
        print(first_point, second_point, first_point is second_point)

    Вывод:
        (9, -4) (9, -4) True
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

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'

    def __add__(self, coord):
        x, y = coord
        return PatchedPoint(self.x + x, self.y + y)

    def __iadd__(self, coord):
        x, y = coord
        self.move(x, y)
        return self
