# Валидация пароля

# После того как пользователь ввёл свои данные в требуемом формате,
# можно позаботиться и о пароле.
# Напишите функцию password_validation, которая принимает один
# позиционный параметр — пароль, и следующие именованные параметры:

#     min_length — минимальная длина пароля, по умолчанию 8;
#     possible_chars — строка символов, которые могут быть в пароле, по
#     умолчанию латинские буквы и цифры;
#     at_least_one — функция возвращающая логическое значение, по
#     умолчанию str.isdigit.

# Если переданный позиционный параметр не является строкой, вызовите
# исключение TypeError.

# А так же реализуйте собственные исключения:

#     MinLengthError — вызывается, если пароль меньше заданной длины;

#     PossibleCharError — вызывается, если в пароле используется
#     недопустимый символ;

#     NeedCharError — вызывается, если в пароле не найдено ни одного
#     обязательного символа.

# Проверка условий должна происходить в порядке указанном в задании.

# Так как, хороший разработчик никогда не хранит пароли в открытом
# виде, функция, в случае успешного завершения, возвращает хеш пароля.
# Для этого воспользуйтесь функцией sha256 из пакета hashlib и верните
# его шестнадцатеричное представление.

from hashlib import sha256


class MinLengthError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def check_string(arg):
    if type(arg) is not str:
        raise TypeError


def password_validation(password, **kwargs):
    check_string(password)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    min_length = kwargs.get('min_length', 8)
    possible_chars = kwargs.get('possible_chars', chars)
    at_least_one = kwargs.get('at_least_one', str.isdigit)
    if len(password) < min_length:
        raise MinLengthError
    if not all(char in possible_chars for char in password):
        raise PossibleCharError
    if not list(filter(at_least_one, password)):
        raise NeedCharError
    return sha256(password.encode()).hexdigest()
