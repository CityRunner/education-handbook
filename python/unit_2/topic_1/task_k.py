# Автоматизация игры

# Всё в том же детском саду ребята очень любят играть с цифрами.
# Одна из таких игр — перестановка цифр четырёхзначного числа.
# Напишите программу для робота-няни, которая из числа вида abcd составляет
# число badc.

# Формат ввода
# Одно четырёхзначное число.

# Формат вывода
# Одно четырёхзначное число — результат перестановки.


digits = input()
print(digits[1:2] + digits[0:1] + digits[3:4] + digits[2:3])
