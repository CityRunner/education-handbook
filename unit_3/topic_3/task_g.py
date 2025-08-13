"""
Делители

Вашему решению будет предоставлено множество numbers.

Продумайте выражение для генерации словаря, содержащего информацию о делителях каждого из заданных чисел.

Примечание:
    В решении не должно быть ничего, кроме выражения.

Example 1:
    Input:
        numbers = {1, 2, 3, 4, 5}
    Output:
        {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5]}

Example 2:
    Input:
        numbers = {15, 49, 36}
    Output:
        {15: [1, 3, 5, 15], 36: [1, 2, 3, 4, 6, 9, 12, 18, 36], 49: [1, 7, 49]}
"""

numbers = {1, 2, 3, 4, 5}
print({num: [div for div in range(1, num + 1) if num % div == 0]
       for num in numbers})

# Expression:
# {num: [div for div in range(1, num + 1) if num % div == 0] for num in numbers}
