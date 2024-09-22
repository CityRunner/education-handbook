# Не решена
#
# Рассылка сообщений
# Продолжим работу с сервером из прошлой задачи. По пути /users/<id>
# доступен JSON объект пользователя с заданным id.
# Подготовьте текст письма для отправки важной рассылки.
# Если пользователь с заданным идентификатором не найден, выведите
# сообщение «Пользователь не найден».

# Формат ввода
# В первой строке вводится адрес сервера.
# Во второй строке вводится id пользователя, которому требуется
# отправить письмо.
# В последующих строках записано содержание сообщения с форматированными
# вставками любого из полей объекта.

# Формат вывода
# Выведите подготовленное сообщение.

from sys import stdin
from requests import get

url = input()
user_id = int(input())
template = stdin.readlines()

r = get(f'http://{url}/users/{user_id}')
if r.status_code == 404:
    print('Пользователь не найден')
else:
    user = r.json()
    message = ''.join(template).format(
        id=user.get('id', ''),
        username=user.get('username', ''),
        last_name=user.get('last_name', ''),
        first_name=user.get('first_name', ''),
        email=user.get('email', ''))
print(message)
