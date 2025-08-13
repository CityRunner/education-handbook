"""
Простая задача 5.0

Напишите функцию is_prime, которая принимает натуральное число, а возвращает булево значение: True — если переданное число простое, а иначе — False.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример 1:
    Ввод:
        result = is_prime(1001459)
    Вывод:
        result = True

Пример 2:
    Ввод:
        result = is_prime(79701)
    Вывод:
        result = False
"""

def is_prime(num):
    prime_state = num > 1
    if prime_state:
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                return = False
    return True
