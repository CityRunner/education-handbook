# Простая задача 2.0
#
# В банке решили переписать программу для шифрования данных и попросили,
# чтобы вы взяли на себя часть данной задачи. Напишите программу для
# разложения числа на простые множители. Только внимательно,
# ведь работать придётся вновь с простыми числами.
#
# Формат ввода
# Вводится одно натуральное число.
#
# Формат вывода
# Требуется составить математическое выражение — произведение простых
# неубывающих чисел, которое в результате даёт исходное.

def is_prime(input_number):
    if (current_number := input_number) > 1:
        for divider in range(2, int(current_number ** 0.5) + 1):
            if current_number % divider == 0:
                return False
    else:
        return False
    return True


prime_dividers = []
current_divider = 2
while (number := int(input())) <= 0:
    pass
if number > 1 and not is_prime(number):
    while not is_prime(number):
        if number % current_divider == 0:
            number = int(number / current_divider)
            prime_dividers.append(current_divider)
        else:
            while not is_prime(current_divider := current_divider + 1):
                pass
    prime_dividers.append(number)
else:
    prime_dividers.append(number)

expression = str(prime_dividers[0])
for index in range(1, len(prime_dividers)):
    expression += f' * {prime_dividers[index]}'
print(expression)
