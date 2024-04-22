# Магазин

# Кроме черешни в магазине продаётся множество других товаров, которые продаются
# на развес. Давайте автоматизируем расчёт сдачи и для них!

# Формат ввода
# Три натуральных числа:
#     цена товара;
#     вес товара;
#     количество денег у пользователя.

# Формат вывода
# Одно целое число — сдача, которую требуется отдать пользователю


<<<<<<< HEAD
price = int(input())
amount = int(input())
cash = int(input())
total_cost = price * amount
change = cash - total_cost
=======
cart = {"price": int(),
        "amount": int(),
        "cash": int()}

for i in cart:
    cart[i] = int(input())

total_cost = cart["price"] * cart["amount"]
change = cart["cash"] - total_cost

>>>>>>> 29cca75b9a18b79cee30c2119ec4a583721ede21
print(change)
