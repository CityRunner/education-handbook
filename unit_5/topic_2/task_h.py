"""
Дроби v0.5

Следующим этапом разработки будет реализация методов сравнения: >, <, >=, <=, ==, !=.

Примечание
    Будем считать, что пользователь знает о запрете деления на ноль.
    Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
    Ввод:
        a = Fraction(1, 3)
        b = Fraction(1, 2)
        print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

    Вывод:
        False True False True False False

Пример 2
    Ввод:
        a = Fraction(1, 3)
        b = Fraction(6, 2).reverse()
        print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

    Вывод:
        False False True True True True
"""

class Fraction:

    def __init__(self, *args):
        match len(args):
            case 1:
                __num, __den = args[0].split('/')
                self.__num = int(__num)
                self.__den = int(__den)
            case 2:
                self.__num, self.__den = args
        self.__normalize()

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    def __repr__(self):
        return f"Fraction('{self.__num}/{self.__den}')"

    def __neg__(self):
        return Fraction(-self.__num, self.__den)

    def __add__(self, other):
        l_num, r_num, den = self.__convert(other)
        num = l_num + r_num
        return Fraction(num, den)

    def __sub__(self, other):
        l_num, r_num, den = self.__convert(other)
        num = l_num - r_num
        return Fraction(num, den)

    def __iadd__(self, other):
        l_num, r_num, den = self.__convert(other)
        self.__num = l_num + r_num
        self.__den = den
        return self.__normalize()

    def __isub__(self, other):
        l_num, r_num, den = self.__convert(other)
        self.__num = l_num - r_num
        self.__den = den
        return self.__normalize()

    def __mul__(self, other):
        l_num, r_num, den = self.__convert(other)
        num = l_num * r_num
        den = den * den
        return Fraction(num, den)

    def __truediv__(self, other):
        l_num, r_num, den = self.__convert(other)
        num = l_num * den
        den = r_num * den
        return Fraction(num, den)

    def __imul__(self, other):
        l_num, r_num, den = self.__convert(other)
        self.__num = l_num * r_num
        self.__den = den * den
        return self.__normalize()

    def __itruediv__(self, other):
        l_num, r_num, den = self.__convert(other)
        self.__num = l_num * den
        self.__den = r_num * den
        return self.__normalize()

    def __gt__(self, other):
        l_num, r_num, den = self.__convert(other)
        if l_num > r_num:
            return True
        else:
            return False

    def __lt__(self, other):
        l_num, r_num, den = self.__convert(other)
        if l_num < r_num:
            return True
        else:
            return False

    def __ge__(self, other):
        l_num, r_num, den = self.__convert(other)
        if l_num >= r_num:
            return True
        else:
            return False

    def __le__(self, other):
        l_num, r_num, den = self.__convert(other)
        if l_num <= r_num:
            return True
        else:
            return False

    def __eq__(self, other):
        l_num, r_num, den = self.__convert(other)
        if l_num == r_num:
            return True
        else:
            return False

    def __ne__(self, other):
        l_num, r_num, den = self.__convert(other)
        if l_num != r_num:
            return True
        else:
            return False

    def __gcd(self):
        a, b = abs(self.__num), abs(self.__den)
        while (R := a % b) > 0:
            a = b
            b = R
        return b

    def __normalize(self):
        gcd = self.__gcd()
        self.__num //= gcd
        self.__den //= gcd
        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self

    def __convert(self, other):
        l_num, l_den = self.__num, self.__den
        r_num, r_den = other.__num, other.__den
        l_num *= r_den
        r_num *= l_den
        c_den = l_den * r_den
        return l_num, r_num, c_den

    def reverse(self):
        return Fraction(self.__den, self.__num)

    def numerator(self, number=None):
        if number:
            if self.__num < 0:
                self.__num = -number
            else:
                self.__num = number
            self.__normalize()
        else:
            return abs(self.__num)

    def denominator(self, number=None):
        if number:
            self.__den = number
            self.__normalize()
        else:
            return self.__den
