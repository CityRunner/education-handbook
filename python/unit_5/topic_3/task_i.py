# Валидация пользователя

# Используйте две предыдущих функции валидации и напишите функцию
# user_validation, которая принимает именованные аргументы:
#     last_name — фамилия;
#     first_name — имя;
#     username — имя пользователя.

# Если функции был передан неизвестный параметр или не передан один из
# обязательных, то вызовите исключение KeyError.
# Если один из параметров не является строкой, то вызовите исключение
# TypeError.
# Обработка данных должна происходить в порядке: фамилия, имя, имя
# пользователя.
# Если поле заполнено верно, функция возвращает словарь с данными
# пользователя.

# Примечание
# В решении не должно быть вызовов требуемых функций.

class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def check_string(arg):
    if type(arg) is not str:
        raise TypeError


def name_validation(name):
    check_string(name)
    chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if not all(char in chars for char in name):
        raise CyrillicError
    if not name.istitle():
        raise CapitalError
    return name


def username_validation(name):
    check_string(name)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    if not all(char in chars for char in name):
        raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError
    return name


def user_validation(**kwargs):
    keys = ('last_name', 'first_name', 'username')
    if len(kwargs) > 3 or not all(key in kwargs for key in keys):
        raise KeyError
    for arg in kwargs:
        check_string(arg)
    user = {'last_name': name_validation(kwargs.get('last_name')),
            'first_name': name_validation(kwargs.get('first_name')),
            'username': username_validation(kwargs.get('username'))}
    return user
