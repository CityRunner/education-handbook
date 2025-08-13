"""
Удаление данных

Завершим эпопею с сервером из прошлых задач. При DELETE запросе по пути /users/<id> производится удаление пользователя с заданным идентификатором.

Напишите программу, которая удаляет пользователя из системы.

Формат ввода
    В первой строке вводится адрес сервера.
    Во второй строке записан идентификатор пользователя, информацию о котором требуется удалить.

Формат вывода
    Ничего выводить не требуется.

Пример
    Ввод
        # Пользовательский ввод:
        127.0.0.1:5000
        2
        # Данные сервера:
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none"
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none"
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none"
            }
        ]

    Вывод
        # Данные сервера:
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none"
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none"
            }
        ]
"""

from requests import delete

url = input()
user_id = int(input())
r = delete(f'http://{url}/users/{user_id}')
