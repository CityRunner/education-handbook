# Цифровая сумма

# Иногда требуется манипулировать с цифрами чисел. Одно из самых простых
# действий, которое можно совершить — найти сумму цифр числа. Напишите
# программу, чтобы выполнить это действие.

# Формат ввода
# Вводится одно натуральное число.

# Формат вывода
# Требуется вывести одно натуральное число — сумму цифр исходного.


result = int()

while (number := int(input())) <= 0:
    pass
for digit in list(str(number)):
    result += int(digit)
print(result)