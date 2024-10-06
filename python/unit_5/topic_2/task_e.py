"""
Дроби v0.2

Продолжим разработку класса Fraction, который реализует предлагаемые дроби.

Предусмотрите возможность задать отрицательные числитель и/или знаменатель. А также перепишите методы __str__ и __repr__ таким образом, чтобы информация об объекте согласовывалась с инициализацией строкой.

Далее реализуйте оператор математического отрицания — унарный минус.

Примечание
    Будем считать, что пользователь знает о запрете деления на ноль.
    Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
    Ввод:
        a = Fraction(1, 3)
        b = Fraction(-2, -6)
        c = Fraction(-3, 9)
        d = Fraction(4, -12)
        print(a, b, c, d)
        print(*map(repr, (a, b, c, d)))

    Вывод:
        1/3 1/3 -1/3 -1/3
        Fraction('1/3') Fraction('1/3') Fraction('-1/3') Fraction('-1/3')

Пример 2
    Ввод:
        a = Fraction('-1/2')
        b = -a
        print(a, b, a is b)
        b.numerator(-b.numerator())
        a.denominator(-3)
        print(a, b)
        print(a.numerator(), a.denominator())
        print(b.numerator(), b.denominator())

    Вывод:
        -1/2 1/2 False
        1/3 -1/2
        1 3
        1 2
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
