# Слияние данных

# Одна местная компания производит обновление данных о пользователях и
# заодно решили реорганизовать систему хранения. Напишите программу,
# которая обновляет данные о пользователях, записанных в JSON файле.

# Формат ввода
# Пользователь вводит два имени файла. В первом хранится JSON массив пользователей.
# Во втором — массив новых данных. Информация о каждом пользователе представляется
# JSON объектом, в котором обязательно присутствует поле name, описывающее имя
# пользователя. Остальные поля являются дополнительными.

# Формат вывода
# В первый файл запишите информацию о пользователях в виде JSON объекта,
# ключами которого выступают имена пользователей, а значениями — объекты с
# информацией о них. Если какая-либо дополнительная информация о пользователе
# изменяется, то требуется сохранить лексикографически большее значение.

import json

with open(file_name := input(), encoding='UTF-8') as file_in:
    users = json.load(file_in)

with open(input(), encoding='UTF-8') as file_in:
    updates = json.load(file_in)

for update in updates:
    for user in users:
        if user['name'] == update['name']:
            for key, value in update.items():
                if key not in user or value > user[key]:
                    user[key] = value

with open(file_name, 'w', encoding='UTF-8') as file_out:
    records = {}
    for user in users:
        records[user['name']] = {key: value for key, value in user.items()
                                 if key != 'name'}
    json.dump(records, file_out, ensure_ascii=False, indent=2)
