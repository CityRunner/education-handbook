"""
Регистрация нового пользователя

Продолжим работу с сервером из прошлых задач. При POST запросе по пути /users доступна возможность создания новых пользователей. Для этого в данные запроса (data) требуется передать JSON объект с информацией о пользователе (без указания идентификатора).

Напишите программу, которая добавляет нового пользователя в систему.

Формат ввода
    В первой строке вводится адрес сервера.
    В следующих строках вводятся: имя пользователя, фамилия, имя и адрес электронной почты.

Формат вывода
    Ничего выводить не требуется.

Пример
    Ввод
        # Пользовательский ввод:
        127.0.0.1:5000
        fourth
        Петров
        Кирилл
        k.petrov@server.none
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
            },
            {
                "username": "fourth",
                "last_name": "Петров",
                "first_name": "Кирилл",
                "email": "k.petrov@server.none",
                "id": 4
            }
        ]
"""

from requests import post

url = input()
fields = ['username', 'last_name', 'first_name', 'email']
new_user = {f: input() for f in fields}
r = post(f'http://{url}/users', json=new_user)
