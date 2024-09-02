# Дроби v0.3

# Продолжим разработку класса Fraction, который реализует
# предлагаемые дроби.

# Реализуйте бинарные операторы:
# + — сложение дробей, создаёт новую дробь;
# - — вычитание дробей, создаёт новую дробь;
# += — сложение дробей, изменяет дробь, переданную слева;
# -= — вычит

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

# a = Fraction(1, 3)
# b = Fraction(1, 2)
# c = a + b
# print(a, b, c, a is c, b is c)

# a = Fraction(1, 8)
# c = b = Fraction(3, 8)
# b -= a
# print(a, b, c, b is c)
