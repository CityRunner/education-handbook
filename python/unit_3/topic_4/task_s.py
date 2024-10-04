"""
Таблица истинности 2

Продолжим работу с таблицами истинности. Продумайте программу,
которая для введённого сложного логического высказывания строит таблицу истинности.

Формат ввода:
    Вводится логическое выражение от нескольких переменных валидное для языка Python.

Формат вывода:
    Выведите таблицу истинности данного выражения.

Примечание:
    В выражении все переменные заданы заглавными латинскими буквами.
    Обратите внимание на параметры __globals и __locals у функции eval.

Example 1:
    Input:
        not A or B and C
    Output:
        A B C F
        0 0 0 1
        0 0 1 1
        0 1 0 1
        0 1 1 1
        1 0 0 0
        1 0 1 0
        1 1 0 0
        1 1 1 1

Example 2:
    Input:
        A and not B and A
    Output:
        A B F
        0 0 0
        0 1 0
        1 0 1
        1 1 0
"""

from itertools import product

expression = input()
variables = sorted(set(filter(str.isupper, expression)))
combos = product(range(2), repeat=len(variables))
table = [combo +
         (int(eval(expression, {},
                   {var: val for var, val in zip(variables, combo)})),)
         for combo in combos]
print(*variables, 'F')
for row in table:
    print(*row)
