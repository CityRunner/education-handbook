"""
Дроби v0.1

Возможно, вы уже заметили, что дробные числа (float) недостаточно точные для некоторых задач. Для более точных математических расчётов иногда прибегают к созданию правильных рациональных дробей, описываемых числителем и знаменателем.

Начнём разработку класса Fraction, который реализует предлагаемые дроби.

Предусмотрите возможность инициализации дроби с помощью двух целых чисел или строки в формате <числитель>/<знаменатель>.
В случаях наличия общего делителя у числителя и знаменателя, дробь следует сократить.

А также реализуйте методы:

    numerator() — возвращает значение числителя;
    numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
    denominator() – возвращает значение знаменателя;
    denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
    __str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
    __repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>).

Примечание
    Будем считать, что пользователь знает о запрете деления на ноль.
    Все числа в данной задаче будут положительными.
    Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
    Ввод:
        fraction = Fraction(3, 9)
        print(fraction, repr(fraction))
        fraction = Fraction('7/14')
        print(fraction, repr(fraction))

    Вывод:
        1/3 Fraction(1, 3)
        1/2 Fraction(1, 2)

Пример 2
    Ввод:
        fraction = Fraction(3, 210)
        print(fraction, repr(fraction))
        fraction.numerator(10)
        print(fraction.numerator(), fraction.denominator())
        fraction.denominator(2)
        print(fraction.numerator(), fraction.denominator())

    Вывод:
        1/70 Fraction(1, 70)
        1 7
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
        self.__reduce()

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    def __repr__(self):
        return f'Fraction({self.__num}, {self.__den})'

    def __gcd(self):
        a, b = self.__num, self.__den
        while (R := a % b) > 0:
            a = b
            b = R
        return b

    def __reduce(self):
        gcd = self.__gcd()
        self.__num //= gcd
        self.__den //= gcd

    def numerator(self, number=None):
        if number:
            self.__num = number
            self.__reduce()
        else:
            return self.__num

    def denominator(self, number=None):
        if number:
            self.__den = number
            self.__reduce()
        else:
            return self.__den
