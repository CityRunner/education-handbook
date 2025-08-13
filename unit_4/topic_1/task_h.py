"""
А роза упала на лапу Азора 7.0

Напишите функцию is_palindrome, которая принимает натуральное число, строку, кортеж или список, а возвращает логическое значение: True — если передан палиндром, а в противном случае — False.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Для определения типа параметра можно воспользоваться функцией type или более продвинутой isinstance.

Пример 1:
    Ввод:
        result = is_palindrome(123)
    Вывод:
        result = False

Пример 2:
    Ввод:
        result = is_palindrome([1, 2, 1, 2, 1])
    Вывод:
        result = True
"""

def is_palindrome(data):
    match type(data).__name__:
        case 'str' | 'tuple':
            return data == data[::-1]
        case 'int':
            return data == int(str(data)[::-1])
        case 'list':
            return data == list(reversed(data))

