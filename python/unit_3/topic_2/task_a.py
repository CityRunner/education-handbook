# Символическая выжимка

# Во многих промышленных задачах требуется понимать, из каких символов
# состоят данные. Напишите программу, чтобы по введённой строке она
# определяла, из каких символов та состоит.

# Формат ввода
# Вводится одна строка.

# Формат вывода
# Требуется вывести все символы этой строки без повторений.
# Порядок вывода не имеет значения.


output = ''
for letter in set(input()):
    output += letter
print(output)
