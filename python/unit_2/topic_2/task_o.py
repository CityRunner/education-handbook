# Властелин Чисел: Возвращение Цезаря
#
# До победы над злом остался один шаг — разрушить логово Зерона.
# Для этого нужно создать трёхзначное магическое число,
# которое будет сильнее двух двухзначных защитных чисел Зерона.
# Самый простой способ создать сильное число:
#     первой взять максимальную цифру из всех защитных чисел;
#     последней — минимальную;
#     в середину поставить сумму оставшихся без учёта переноса разряда.
# Помогите одолеть зло.
#
# Формат ввода
# В двух строках записаны защитные числа Зерона.
#
# Формат вывода
# Одно трёхзначное число, которое приведёт к победе.

first_number = second_number = '0'

while int(first_number) not in range(10, 100) or int(second_number) not in range(10, 100):
    first_number = input()
    second_number = input()

digits = sorted(list(first_number + second_number))
magic_number = digits[3] + str((int(digits[1]) + int(digits[2])) % 10) + digits[0]

print(magic_number)