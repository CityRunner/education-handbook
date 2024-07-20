# Файловая чистка

# Python в первую очередь скриптовый язык. Такие языки часто используются
# для создания консольных утилит. Напишите простую утилиту,
# которая очищает заданный файл от:
# - повторяющихся пробелов;
# - повторяющихся символов перевода строки;
# - табуляций;
# - излишних пробелов в начале и конце строк.

# Формат ввода
# Пользователь вводит два имени файлов. Входной файл содержит
# неформатированный текст произвольной длины.

# Формат вывода
# Во второй файл выведите очищенный текст.

with open(input(), encoding='UTF-8') as file_in:
    lines = file_in.readlines()

clean_lines = []
for line in lines:
    line = line.replace('\t', '').replace('\n', '').strip()
    while '  ' in line:
        line = line.replace('  ', ' ')
    if any(line):
        clean_lines.append(line)

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write('\n'.join(line for line in clean_lines))
