# Разделяй и властвуй

# Напишите утилиту, которая разделяет числа, записанные в файле, на три
# группы:
#  числа с преобладающим количеством чётных цифр;
#  числа с преобладающим количеством нечётных цифр;
#  числа с одинаковым количеством чётных и нечётных цифр.

# Формат ввода
# Пользователь вводит четыре имени файла. Первый файл содержит
# произвольное количество чисел, разделённых пробелами и символами
# перевода строки.

# Формат вывода
# В три другие файла выведите числа, которые подходят под требуемое
# условие. Сохраните положение чисел в строках.

results = {'evens': [], 'odds': [], 'eqs': []}

with open(input(), encoding='UTF-8') as file_in:
    lines = [line for line in file_in.readlines()]

for line in lines:
    evens_line = []
    odds_line = []
    eqs_line = []
    for num in line.split():
        digits = list(num)
        even = [digit for digit in digits if int(digit) % 2 == 0]
        odd = [digit for digit in digits if int(digit) % 2 != 0]
        if len(even) > len(odd):
            evens_line.append(num)
        elif len(even) < len(odd):
            odds_line.append(num)
        elif len(even) == len(odd):
            eqs_line.append(num)
    results['evens'].append(evens_line)
    results['odds'].append(odds_line)
    results['eqs'].append(eqs_line)

for value in results.values():
    with open(input(), 'w', encoding='UTF-8') as file_out:
        file_out.write('\n'.join(' '.join(num for num in line)
                                 for line in value) + '\n')
