"""
Классная точка 2.0

Давайте расширим функционал класса, написанного в прошлой задаче.

Реализуйте методы:

    move, который перемещает точку на заданное расстояние по осям xx и yy;
    length, который определяет до переданной точки расстояние, округлённое до сотых.

Примечание:
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1:
    Ввод:
        point = Point(3, 5)
        print(point.x, point.y)
        point.move(2, -3)
        print(point.x, point.y)

    Вывод:
        3 5
        5 2

Пример 2:
    Ввод:
        first_point = Point(2, -7)
        second_point = Point(7, 9)
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
