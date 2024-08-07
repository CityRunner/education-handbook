# А роза упала на лапу Азора 7.0

# Напишите функцию is_palindrome, которая принимает натуральное
# число, строку, кортеж или список, а возвращает логическое значение:
# True — если передан палиндром, а в противном случае — False.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# Для определения типа параметра можно воспользоваться функцией
# type или более продвинутой isinstance.

def is_palindrome(data):
    match type(data).__name__:
        case 'str':
            reverse = data[::-1]
        case 'tuple':
            reverse = data[::-1]
        case 'int':
            reverse = int(str(data)[::-1])
        case 'list':
            reverse = list(reversed(data))
    return data == reverse


# result = is_palindrome(123)
# print(result)
