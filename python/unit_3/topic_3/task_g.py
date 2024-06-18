# Делители

# Вашему решению будет предоставлено множество numbers.
# Продумайте выражение для генерации словаря содержащего информацию
# о делителях каждого из заданных чисел.

# Примечание
# В решении не должно быть ничего, кроме выражения.

print('Enter numbers divided by a single space (e.g., "15 49 36")')
numbers = {int(number) for number in input('numbers = ').split()}
print({num: [div for div in range(1, num + 1) if num % div == 0]
       for num in numbers})

# Expression:
# {num: [div for div in range(1, num + 1) if num % div == 0] for num in numbers}
