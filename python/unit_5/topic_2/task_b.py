# Классная точка 4.0

# А теперь модернизируем уже новый класс PatchedPoint. Реализуйте
# магические методы __str__ и __repr__.

# При преобразовании в строку точка представляется в формате (x, y).
# Репрезентация же должна возвращать строку для инициализации точки
# двумя параметрами.

# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

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


# point = PatchedPoint()
# print(point)
# point.move(2, -3)
# print(repr(point))

# first_point = PatchedPoint((2, -7))
# second_point = PatchedPoint(7, 9)
# print(*map(str, (first_point, second_point)))
# print(*map(repr, (first_point, second_point)))

