# Чек

# Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так
# просто.

# Формат ввода
#     название товара;
#     цена товара;
#     вес товара;
#     количество денег у пользователя.

# Формат вывода
# Чек
# <название товара> - <вес>кг - <цена>руб/кг
# Итого: <итоговая стоимость>руб
# Внесено: <количество денег от пользователя>руб
# Сдача: <сдача>руб


name = input()
price = int(input())
amount = int(input())
cash = int(input())

total_cost = price * amount
change = cash - total_cost

print(f'''Чек\n{name} - {amount}кг - {price}руб/кг
Итого: {total_cost}руб\nВнесено: {cash}руб\nСдача: {change}руб''')
