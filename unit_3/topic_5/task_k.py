"""
Файловая статистика 2.0

Напишите программу, которая для заданного файла вычисляет следующие параметры:

    количество всех чисел;
    количество положительных чисел;
    минимальное число;
    максимальное число;
    сумма всех чисел;
    среднее арифметическое всех чисел с точностью до двух знаков после запятой.

Формат ввода:
    Пользователь вводит два имени файла.
    Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.

Формат вывода:
    Выведите статистику во второй файл в формате JSON.

Ключи значений задайте соответственно:

    count — количество всех чисел;
    positive_count — количество положительных чисел;
    min — минимальное число;
    max — максимальное число;
    sum — сумма всех чисел;
    average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.

Пример:
    Ввод:
        # Пользовательский ввод:
        numbers.txt
        statistics.json

        # Содержимое файла numbers.txt
        1 2 3 4 5
        -5 -4 -3 -2 -1
        10 20
        20 10

    Вывод:
        # Содержимое файла statistics.json
        {
            "count": 14,
            "positive_count": 9,
            "min": -5,
            "max": 20,
            "sum": 60,
            "average": 4.29
        }
"""

import json

with open(input(), encoding='UTF-8') as file_in:
    nums = [int(num) for num in file_in.read().split()]
    nums_pos = len([num for num in nums if num > 0])
    nums_mean = round(sum(nums) / len(nums), 2)

records = {'count': len(nums),
           'positive_count': nums_pos,
           'min': min(nums),
           'max': max(nums),
           'sum': sum(nums),
           'average': nums_mean}

with open(input(), 'w', encoding='UTF-8') as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)
