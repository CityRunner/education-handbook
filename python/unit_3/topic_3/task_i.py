# Преобразование в строку

# Вашему решению предоставлен список натуральных чисел numbers.
# Напишите выражение для генерации строки, представляющей собой
# отсортированный список чисел, записанных через дефис, окружённый
# пробелами, без повторений.

# Примечание
# В решении не должно быть ничего, кроме выражения.

print('Enter numbers divided by a single space (e.g., "3 1 2 3 2 2 1")')
numbers = [int(number) for number in input('numbers = ').split()]
print(' - '.join([str(num) for num in sorted(set(numbers))]))

# Expression:
# ' - '.join([str(num) for num in sorted(set(numbers))])
