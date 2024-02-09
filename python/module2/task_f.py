cart = {"name": "", "price": 0, "amount": 0, "cash": 0}
for i in cart:
    cart[i] = input()
total_cost = int(cart["price"]) * int(cart["amount"])
change = int(cart["cash"]) - int(total_cost)
print(f"""Чек
{cart["name"]} - {cart["amount"]}кг - {cart["price"]}руб/кг
Итого: {total_cost}руб
Внесено: {cart["cash"]}руб
Сдача: {change}руб
""")
