"""
Однотипность не порок

Во многих задачах требуется контроль входных данных, в частности, несмотря на динамическую типизацию, их типов.

Разработайте декоратор same_type, который производит проверку переменного количества позиционных параметров. В случае получения не одинаковых типов выводит сообщение "Обнаружены различные типы данных" и прерывает выполнение функции.

Примечание:
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1:
    Ввод:
        @same_type
        def a_plus_b(a, b):
            return a + b

        print(a_plus_b(3, 5.2) or 'Fail')
        print(a_plus_b(7, '9') or 'Fail')
        print(a_plus_b(-3, 5) or 'Fail')

    Вывод:
        Обнаружены различные типы данных
        Fail
        Обнаружены различные типы данных
        Fail
        2

Пример 2:
    Ввод:
        @same_type
        def combine_text(*words):
            return ' '.join(words)

        print(combine_text('Hello,', 'world!') or 'Fail')
        print(combine_text(2, '+', 2, '=', 4) or 'Fail')
        print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')

    Вывод:
        Hello, world!
        Обнаружены различные типы данных
        Fail
        Обнаружены различные типы данных
        Fail
"""

def same_type(func):

    def decorated(*args):
        first_type = type(args[0])
        if all(type(arg) is first_type for arg in args[1:]):
            return func(*args)
        else:
            print('Обнаружены различные типы данных')
    return decorated
