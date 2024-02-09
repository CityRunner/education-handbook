card = {"name": '',
        "locker": 0,
        "group": 0,
        "id": 0,
        "bed": 0}

while card["name"] == '' or (card["locker"] not in range(100, 1000)):
    card["name"] = input()
    card["locker"] = int(input())

card["group"] = card["locker"] // 100
card["id"] = card["locker"] % 10
card["bed"] = card["locker"] // 10 % 10

print(f"""Группа №{card["group"]}.
{card["id"]}. {card["name"]}.
Шкафчик: {card["locker"]}.
Кроватка: {card["bed"]}.""")
