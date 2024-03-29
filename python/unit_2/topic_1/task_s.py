# Украшение чека

# Давайте приведём в порядок чек, который печатали ранее.
# Все строки должны быть длиной в 35 символов.

# Формат ввода
#     Название товара;
#     цена товара;
#     вес товара;
#     количество денег у пользователя.

# Формат вывода
# Красивый чек в формате:
# ================Чек================
# Товар:                    <продукт>
# Цена:     <число>кг * <число>руб/кг
# Итого:                   <число>руб
# Внесено:                 <число>руб
# Сдача:                   <число>руб
# ===================================

# Примечание
# В данный момент примеры ниже визуализируются неправильно.


name = None
price = mass = cash = int()

while not name or price <= 0 or mass <= 0 or cash <= 0:
    name = input()
    price = int(input())
    mass = int(input())
    cash = int(input())

total = mass * price
change = cash - total

spaces = {"name": " " * (29 - len(name)),
          "price": " " * (19 - len(str(mass)) - len(str(price))),
          "total": " " * (26 - len(str(total))),
          "cash": " " * (24 - len(str(cash))),
          "change": " " * (26 - len(str(change)))}

check = f"""================Чек================
Товар:{spaces["name"]}{name}
Цена:{spaces["price"]}{mass}кг * {price}руб/кг
Итого:{spaces["total"]}{total}руб
Внесено:{spaces["cash"]}{cash}руб
Сдача:{spaces["change"]}{change}руб
==================================="""

print(check)
