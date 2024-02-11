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
