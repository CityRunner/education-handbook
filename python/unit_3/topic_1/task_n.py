# Массовое возведение в степень 2.0

# Продолжим упрощать себе работу, минуя множество одинаковых операций. Создадим
# новую программу, которая возводит в заданную степень все числа, переданные
# пользователем.

# Формат ввода
# В первой строке записана последовательность натуральных чисел, разделённых
# пробелами.
# Во второй строке записано натуральное число P — степень, в которую требуется
# возвести числа.

# Формат вывода
# Последовательность чисел, являющихся ответом.
# Числа вывести в одну строку через пробел.

numbers = input().split(' ')
exponent = int(input())
result_list = []

for number in numbers:
    if exponent == 0:
        result_list.append('1')
    elif exponent == 1:
        result_list.append(number)
    else:
        result = int(number)
        for _ in range(1, exponent):
            result *= int(number)
        result_list.append(str(result))

print(' '.join(result_list))
