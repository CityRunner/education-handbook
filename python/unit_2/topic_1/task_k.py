# Автоматизация игры

# Всё в том же детском саду ребята очень любят играть с цифрами.
# Одна из таких игр — перестановка цифр четырёхзначного числа.
# Напишите программу для робота-няни, которая из числа вида abcd составляет
# число badc.

# Формат ввода
# Одно четырёхзначное число.

# Формат вывода
# Одно четырёхзначное число — результат перестановки.


numbers = None

while numbers not in range(1000, 10000):
    numbers = int(input())

letters = str(numbers)
srebmun = int(letters[1:2] + letters[0:1] + letters[3:4] + letters[2:3])

print(srebmun)
