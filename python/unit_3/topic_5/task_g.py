# Файловая статистика

# Напишите программу, которая для заданного файла вычисляет следующие
# параметры:
# - количество всех чисел;
# - количество положительных чисел;
# - минимальное число;
# - максимальное число;
# - сумма всех чисел;
# - среднее арифметическое всех чисел с точностью до двух знаков после запятой.

# Формат ввода
# Пользователь вводит имя файла. Файл содержит произвольное количество
# чисел, разделённых пробелами и символами перевода строки.

# Формат вывода
# Выведите статистику в указанном порядке.

with open(input(), encoding='UTF-8') as file_in:
    nums = [int(num) for num in file_in.read().split()]

print(len(nums))
print(len([num for num in nums if num > 0]))
print(min(nums))
print(max(nums))
print(sum(nums))
print(round(sum(nums) / len(nums), 2))