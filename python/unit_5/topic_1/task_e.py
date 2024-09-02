# Классный прямоугольник

# Давайте перейдём к более сложным геометрическим фигурам.
# Разработайте класс Rectangle.
# При инициализации класс принимает два кортежа рациональных
# координат противоположных углов прямоугольника (со сторонами
# параллельными осям координат).

# Класс должен реализовывать методы:
#     perimeter — возвращает периметр прямоугольника;
#     area — возвращает площадь прямоугольника.
# Все результаты вычислений нужно округлить до сотых.

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

# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.perimeter())

# rect = Rectangle((7.52, -4.3), (3.2, 3.14))
# print(rect.area())


