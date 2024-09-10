# Валидация имени пользователя

# Продолжим реализацию системы валидации.
# Напишите функцию username_validation, которая принимает один
# позиционный аргумент — имя пользователя:
# Если параметр не является строкой, то вызовите исключение TypeError.
# А также разработайте собственные ошибки:
#     BadCharacterError — вызывается, если значение состоит не только
#     из латинских букв, цифр и символа нижнего подчёркивания;
#     StartsWithDigitError — вызывается, если значение начинается с
#     цифры.
# Обработка ошибок должна происходить в порядке, указанном в задании.
# В случае успешного выполнения, функция должна вернуть переданный
# параметр без изменений.

# Примечание
# В решении не должно быть вызовов требуемых функций.

class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    numbers = range(48, 58)
    lat_num_und = [*range(65, 91), *range(97, 123), *numbers, 95]
    if type(name) is not str:
        raise TypeError
    if not all(ord(sym) in lat_num_und for sym in name):
        raise BadCharacterError
    if any(name.startswith(chr(num)) for num in numbers):
        raise StartsWithDigitError
    return name
