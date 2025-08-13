"""
Обновление данных

Часто приходится обновлять данные.

Создайте программу, которая обновляет JSON файл.

Формат ввода:
    Пользователь вводит имя файла.
    Затем вводятся строки вида ключ == значение.

Формат вывода:
    В заданный пользователем файл следует записать обновленный JSON.

Пример:
    Ввод:
        # Пользовательский ввод:
        data.json
        one == один
        two == два
        three == три

        # Содержимое файла data.json
        {
            "one": 1,
            "three": 2
        }

    Вывод:
        # Содержимое файла data.json
        {
            "one": "один",
            "three": "три",
            "two": "два"
        }
"""

from sys import stdin
import json

with open(file_name := input(), encoding="UTF-8") as file_in:
    records = json.load(file_in)

with open(file_name, 'w', encoding='UTF-8') as file_out:
    for line in stdin.readlines():
        key, value = line.strip('\n').split(' == ')
        records[key] = value
    json.dump(records, file_out, indent=2)
