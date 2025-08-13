"""
Классный прямоугольник 2.0

Расширим функционал класса написанного вами в предыдущей задаче.

Реализуйте методы:

    get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
    get_size() — возвращает размеры в виде кортежа;
    move(dx, dy) — изменяет положение на заданные значения;
    resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).

Примечание:
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.
Все результаты вычислений нужно округлить до сотых.

Пример 1:
    Ввод:
        rect = Rectangle((3.2, -4.3), (7.52, 3.14))
        print(rect.get_pos(), rect.get_size())
        rect.move(1.32, -5)
        print(rect.get_pos(), rect.get_size())

    Вывод:
        (3.2, 3.14) (4.32, 7.44)
        (4.52, -1.86) (4.32, 7.44)

Пример 2:
    Ввод:
        rect = Rectangle((7.52, -4.3), (3.2, 3.14))
        print(rect.get_pos(), rect.get_size())
        rect.resize(23.5, 11.3)
        print(rect.get_pos(), rect.get_size())

    Вывод:
        (3.2, 3.14) (4.32, 7.44)
        (3.2, 3.14) (23.5, 11.3)
"""

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
