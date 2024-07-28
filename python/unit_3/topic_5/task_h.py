# Файловая разница

# Напишите программу, которая определяет, какие слова есть только в одном
# из файлов.

# Формат ввода
# Пользователь вводит три имени файлов. Каждый из входных файлов содержит
# произвольное количество слов, разделённых пробелами и символами
# перевода строки.

# Формат вывода
# В третий файл выведите в алфавитном порядке без повторений список слов,
# которые есть только в одном из файлов.

with open(input(), encoding='UTF-8') as file_in:
    first = set(word for word in file_in.read().split())

with open(input(), encoding='UTF-8') as file_in:
    second = set(word for word in file_in.read().split())

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write('\n'.join(sorted(first ^ second)))
