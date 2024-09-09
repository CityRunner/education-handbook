# Корень зла 2

# В одной из первых лекций вы уже решали задачу о поиске корней
# уравнения. Давайте модернизируем её.

# Напишите функцию find_roots, принимающую три параметра: коэффициенты
# уравнения и возвращающую его корни в виде кортежа из двух значений.
# Так же создайте два собственных исключения NoSolutionsError и
# InfiniteSolutionsError, которые будут вызваны в случае отсутствия и
# бесконечного количества решений уравнения соответственно.

# Если переданные коэффициенты не являются рациональными числами,
# вызовите исключение TypeError.

class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    for x in (a, b, c):
        if not isinstance(x, (int, float, complex)) or isinstance(x, bool):
            raise TypeError
    if a == b == c == 0:
        raise InfiniteSolutionsError
    elif a == b == 0:
        raise NoSolutionsError
    elif a == 0 and b != 0 and c != 0:
        return (-(c / b), -(c / b))
    else:
        D = b ** 2 - 4 * a * c
        if D == 0:
            return (-b / (2 * a), -b / (2 * a))
        elif D > 0:
            x1 = (-b - (D ** 0.5)) / (2 * a)
            x2 = (-b + (D ** 0.5)) / (2 * a)
            return tuple(sorted([x1, x2]))
        else:
            raise NoSolutionsError
