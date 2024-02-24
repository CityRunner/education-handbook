# Простая задача 3.0

# Вспомним, что простые числа — те натуральные числа, у которых два делителя:
# оно само и 1. Напишите программу для определения количества простых чисел
# среди введённых.

# Формат ввода
# В первой строке записано число N.
# Во всех последующих N строках — по одному числу.

# Формат вывода
# Требуется вывести общее количество простых чисел среди введённых (кроме N).


def is_prime(input_number):
    if (current_number := input_number) > 1:
        for divider in range(2, int(current_number ** 0.5) + 1):
            if current_number % divider == 0:
                return False
    else:
        return False
    return True


primes = int()

for count in range(int(input())):
    if is_prime(int(input())):
        primes += 1

print(primes)

