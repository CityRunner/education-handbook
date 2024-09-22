# Суммирование ответов 2

# Сервер отвечает на запрос JSON списком.
# Выведите сумму чисел в полученном списке.

# Формат ввода
# Вводится адрес сервера

# Формат вывода
# Одно число — сумма всех чисел в полученном списке.

from requests import get

url = input()
r = get(f'http://{url}')
num_sum = sum(num for num in r.json() if type(num) is int)
print(num_sum)
