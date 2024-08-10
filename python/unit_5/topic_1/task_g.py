# Классный прямоугольник 3.0

# Необходимо ещё немного доработать предыдущую задачу.

# Разработайте методы:
#     turn() — поворачивает прямоугольник на 90° по часовой стрелке
#     вокруг его центра;
#     scale(factor) — изменяет размер в указанное количество раз, тоже
#     относительно центра.
# Все вычисления производить с округлением до сотых.

# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Rectangle:

    def __init__(self, a, c):
        self.a = a
        self.c = c
        self.set_coordinates(sort=True)

    def set_coordinates(self, sort=False):
        self.b = (self.a[0], self.c[1])
        self.d = (self.c[0], self.a[1])
        if sort:
            coords = [self.a, self.b, self.c, self.d]
            from_top_left = sorted(coords, key=lambda x: [x[0], -x[1]])
            self.a, self.d, self.b, self.c = from_top_left

    def get_size(self):
        w = abs(self.c[0] - self.a[0])
        h = abs(self.c[1] - self.a[1])
        return (round(w, 2), round(h, 2))

    def perimeter(self):
        w, h = self.get_size()
        p = 2 * (w + h)
        return round(p, 2)

    def area(self):
        w, h = self.get_size()
        s = w * h
        return round(s, 2)

    def get_pos(self):
        return self.a

    def move(self, dx, dy):
        self.a = (round(self.a[0] + dx, 2), round(self.a[1] + dy, 2))
        self.c = (round(self.c[0] + dx, 2), round(self.c[1] + dy, 2))
        self.set_coordinates()

    def resize(self, w, h):
        x = round(w + self.a[0], 2)
        y = round(h + self.a[1], 2)
        self.c = (x, y)
        self.set_coordinates()

    def turn(self):
        half_w = (self.c[0] - self.a[0]) / 2
        half_h = (self.c[1] - self.a[1]) / 2
        mid_x = (self.a[0] + self.c[0]) / 2
        mid_y = (self.a[1] + self.c[1]) / 2
        self.a = (mid_x - half_h, mid_y - half_w)
        self.c = (mid_x + half_h, mid_y + half_w)
        self.set_coordinates(sort=True)

    def scale(self, factor):
        w, h = self.get_size()
        new_w = w * factor
        new_h = h * factor
        mid_x = (self.a[0] + self.c[0]) / 2
        mid_y = (self.a[1] + self.c[1]) / 2
        self.a = (mid_x - new_w / 2, mid_y - new_h / 2)
        self.c = (mid_x + new_w / 2, mid_y + new_h / 2)
        self.set_coordinates(sort=True)

# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.turn()
# print(rect.get_pos(), rect.get_size(), sep='\n')
