# Суммарная сумма

# Найти сумму цифр числа не так сложно, но что, если чисел несколько?
# Напишите программу для выполнения этого действия.

# Формат ввода
# В первой строке указано число N Во всех последующих N строках написано по
# одному числу.

# Формат вывода
# Требуется вывести общую сумму цифр всех введённых чисел (кроме N).


summ = 0

for count in range(int(input())):
    for digit in input():
        summ += int(digit)

print(summ)