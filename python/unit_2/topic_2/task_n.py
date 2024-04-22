# Властелин Чисел: Две Башни

# Во времена, когда люди верили в великую силу чисел, оказалось, что волшебник
# Пифуман предал все народы и стал помогать Зерону.

# Чтобы посетить башни обоих злодеев одновременно, нам следует разделить магию
# числа, которое защищало нас в дороге.

# Чтобы поделить трёхзначное число, нам нужно составить из него минимально и
# максимально возможные двухзначные числа.

# Формат ввода
# Одно трёхзначное число.

# Формат вывода
# Два защитных числа для каждого отряда, записанные через пробел.


digits = sorted(list(input()))
if digits[0] != '0':
    min_number = digits[0] + digits[1]
else:
    min_number = digits[1] + digits[0]
max_number = digits[2] + digits[1]

print(min_number, max_number)
