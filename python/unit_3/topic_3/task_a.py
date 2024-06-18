# Список квадратов

# Большинство задач этой главы ориентированы на отработку навыков
# по построению списочных выражений.
# Вашему решению будет предоставлены две переменные a и b.
# Напишите списочное выражение для получения квадратов чисел из
# диапазона [a,b].

# Примечание
# В решении не должно быть ничего, кроме списочного выражения.

print('Enter two numbers, one per line')
a, b = int(input('a = ')), int(input('b = '))
print([number ** 2 for number in range(a, b + 1)])

# Expression:
# [number ** 2 for number in range(a, b + 1)]
