"""
Разделяй и властвуй

Напишите утилиту, которая разделяет числа, записанные в файле, на три группы:

    числа с преобладающим количеством чётных цифр;
    числа с преобладающим количеством нечётных цифр;
    числа с одинаковым количеством чётных и нечётных цифр.

Формат ввода:
    Пользователь вводит четыре имени файла.
    Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.

Формат вывода:
    В три другие файла выведите числа, которые подходят под требуемое условие.
    Сохраните положение чисел в строках.

Пример:
    Ввод:
        # Пользовательский ввод:
        numbers.txt
        even.txt
        odd.txt
        eq.txt

        # Содержимое файла numbers.txt
        650975472 591084323 629700 1504180 577023
        8460612246 42161437 29409368 58531725 5725268 2198001838
        796451 69358 7195510 975628465 9756641
        44200289 126541 979391 93479581 291170 28987042 86139603

    Вывод:
        # Содержимое файла even.txt
        629700 1504180
        8460612246 29409368 5725268 2198001838
        975628465
        44200289 28987042

        # Содержимое файла odd.txt
        650975472 591084323 577023
        58531725
        796451 69358 7195510 9756641
        979391 93479581 291170

        # Содержимое файла eq.txt
        42161437

        126541 86139603
"""

with open(input(), encoding='UTF-8') as file_in:
    lines = [line for line in file_in.readlines()]

nums = {'evens': [], 'odds': [], 'eqs': []}
for line in lines:
    evens = []
    odds = []
    eqs = []
    for num in line.split():
        digits = list(num)
        even = [d for d in digits if int(d) % 2 == 0]
        odd = [d for d in digits if int(d) % 2 != 0]
        if len(even) > len(odd):
            evens.append(num)
        elif len(even) < len(odd):
            odds.append(num)
        elif len(even) == len(odd):
            eqs.append(num)
    nums['evens'].append(evens)
    nums['odds'].append(odds)
    nums['eqs'].append(eqs)

for value in nums.values():
    with open(input(), 'w', encoding='UTF-8') as file_out:
        file_out.write('\n'.join(' '.join(line) for line in value) + '\n')
