price = 38
amount = 2.5
cash = 0
while cash < 100:
    cash = int(input())
total_cost = price * amount
change = cash - int(total_cost)
print(change)
