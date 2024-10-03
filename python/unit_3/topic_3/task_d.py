"""
Множество нечетных чисел

Вашему решению будет предоставлен список numbers, содержащий натуральные числа.

Напишите выражение для генерации множества всех нечётных чисел среди переданных.

Примечание:
    В решении не должно быть ничего, кроме выражения.

Example 1:
    Input:
        numbers = [1, 2, 3, 4, 5]
    Output:
        {1, 3, 5}

Example 2:
    Input:
        numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
    Output:
        {1, 3}
"""

numbers = [1, 2, 3, 4, 5]
print({number for number in numbers if number % 2 != 0})

# Expression:
# {number for number in numbers if number % 2 != 0}
