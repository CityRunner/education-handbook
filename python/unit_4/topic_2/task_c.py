# Функциональный нод 2.0

# Напишите функцию gcd, которая вычисляет наибольший общий
# делитель последовательности чисел. Параметрами функции выступают
# натуральные числа в произвольном количестве, но не менее одного.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def gcd(*args):
    a, *numbers = args
    for b in numbers:
        while R := a % b:
            a, b = b, R
        a = b
    return a


# result = gcd(36, 48, 156, 100500)
# print(result)