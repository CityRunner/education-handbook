# НОК

# Спустя время НИИ потребовалось находить наименьшее общее кратное (НОК)
# двух чисел. К нам вновь обратились за помощью.

# Формат ввода
# Вводится два натуральных числа, каждое на своей строке.

# Формат вывода
# Требуется вывести одно натуральное число - НОК двух данных чисел.


a = int(input())
b = int(input())
N = 1
while (N % a != 0) or (N % b != 0):
    N += 1
print(N)