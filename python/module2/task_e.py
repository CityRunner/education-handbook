cart = {"price": 0, "amount": 0, "cash": 0}
for i in cart:
    cart[i] = int(input())
total_cost = cart["price"] * cart["amount"]
change = cart["cash"] - int(total_cost)
print(change)
