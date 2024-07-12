# Множество нечетных чисел

# Вашему решению будет предоставлен список numbers, содержащий
# натуральные числа.
# Напишите выражение для генерации множества всех нечётных чисел
# среди переданных.

# Примечание
# В решении не должно быть ничего, кроме выражения.

print('Enter numbers divided by a single space (e.g., "1 2 3 4 5")')
numbers = [int(number) for number in input('numbers = ').split()]
print({number for number in numbers if number % 2 != 0})

# Expression:
# {number for number in numbers if number % 2 != 0}
