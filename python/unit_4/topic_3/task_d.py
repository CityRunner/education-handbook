"""
Декор результата

Напишите декоратор answer, который преобразует функцию, принимающую неограниченное число позиционных и именованных параметров и возвращает её результат с припиской "Результат функции: <значение>".

Примечание

Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1:
    Ввод:
        @answer
        def a_plus_b(a, b):
            return a + b

        print(a_plus_b(3, 5))
        print(a_plus_b(7, 9))

    Вывод:
        Результат функции: 8
        Результат функции: 16

Пример 2:
    Ввод:
        @answer
        def get_letters(text: str) -> str:
            return ''.join(sorted(set(filter(str.isalpha, text.lower()))))

        print(get_letters('Hello, world!'))
        print(get_letters('Декораторы это круто =)'))

    Вывод:
        Результат функции: dehlorw
        Результат функции: адекортуыэ
"""

def answer(func):

    def decorated(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return decorated
