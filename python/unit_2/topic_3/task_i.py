# Факториал

# Учёным срочно нужно ПО, которое находит факториал числа.

# Формат ввода
# Вводится одно неотрицательное число.

# Формат вывода
# Требуется вывести одно натуральное число - факториал заданного числа.

# Примечания
# Факториал нуля принят равным 1.


F = 1

number = int(input())

if number > 0:
    for i in range(number, 1, -1):
        F *= i
    print(F)
elif number == 0:
    print(1)