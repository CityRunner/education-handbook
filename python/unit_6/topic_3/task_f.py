"""
Список пользователей

На сервере по пути /users, доступен список пользователей, представленных JSON объектами с ключами:
    id — уникальный идентификатор пользователя;
    username — имя пользователя;
    last_name — фамилия;
    first_name — имя;
    email — адрес электронной почты.

Формат ввода
    В первой строке вводится адрес сервера.

Формат вывода
    Выведите список всех пользователей системы в алфавитном порядке.

Пример
    Ввод
        # Пользовательский ввод:
        127.0.0.1:5000
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
        Иванов Василий
        Иванов Виктор
        Петрова Елизавета
"""

from requests import get

url = input()
r = get(f'http://{url}/users')
users = [f'{user["last_name"]} {user["first_name"]}' for user in r.json()]
print('\n'.join(sorted(users)))
