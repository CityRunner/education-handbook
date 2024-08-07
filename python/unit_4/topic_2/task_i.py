# Чётная фильтрация

# Напишите lambda выражение для фильтрации чисел с чётной суммой цифр.

# Примечание
# В решении не должно быть ничего, кроме выражения.

print(*filter(lambda n: sum(int(d) for d in str(n)) % 2 == 0, (1, 2, 3, 4, 5)))

# Expression
# lambda n: sum(int(d) for d in str(n)) % 2 == 0
