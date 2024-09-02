# Дроби v0.7

# "Остался последний штрих!" Правда звучит как издевательство?
# Мы «научили» наши дроби работать с целыми числами и вот теперь
# надо провернуть обратное действие. Реализуйте функционал, который
# позволит производить все арифметические операции с дробями и
# числами, независимо от их положения (слева или справа) в операторе.

# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать
# (называть с использованием ведущих символов нижнего подчёркивания).
# Ваше решение должно содержать только классы и функции. В решении
# не должно быть вызовов инициализации требуемых классов.

class Fraction:

    def __init__(self, arg, opt=None):
        if opt:
            self.__num = arg
            self.__den = opt
        else:
            if type(arg) is int:
                self.__num = arg
                self.__den = 1
            elif type(arg) is str:
                if '/' in arg:
                    num, den = arg.split('/')
                    self.__num = int(num)
                    self.__den = int(den)
                else:
                    self.__num = int(arg)
                    self.__den = 1
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

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        l_num, r_num, den = self.__convert(other)
        self.__num = l_num + r_num
        self.__den = den
        return self.__normalize()

    def __sub__(self, other):
        l_num, r_num, den = self.__convert(other)
        num = l_num - r_num
        return Fraction(num, den)

    def __rsub__(self, other):
        return -self.__sub__(other)

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

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        l_num, r_num, den = self.__convert(other)
        self.__num = l_num * r_num
        self.__den = den * den
        return self.__normalize()

    def __truediv__(self, other):
        l_num, r_num, den = self.__convert(other)
        num = l_num * den
        den = r_num * den
        return Fraction(num, den)

    def __rtruediv__(self, other):
        return self.__truediv__(other).reverse()

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
        if type(other) is int:
            r_num, r_den = other, 1
        else:
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

# a = Fraction(1)
# b = Fraction('2')
# c, d = map(Fraction.reverse, (2 + a, -1 + b))
# print(a, b, c, d)
# print(a > b, c > d)
# print(a >= 1, b >= 1, c >= 1, d >= 1)

# a = Fraction(1, 2)
# b = Fraction('2/3')
# c, d = map(Fraction.reverse, (3 - a, 2 / b))
# print(a, b, c, d)
# print(a > b, c > d)
# print(a >= 1, b >= 1, c >= 1, d >= 1)
