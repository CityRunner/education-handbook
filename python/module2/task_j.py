# Детский сад — штаны на лямках
#
# В продолжение темы детского сада давайте и там что-нибудь автоматизируем.
# За каждым ребёнком закреплён шкафчик и кровать. Номер шкафчика состоит из трёх цифр:
#     номер группы в саду;
#     номер кроватки закреплённой за ребёнком;
#     порядковый номер ребёнка в списке группы.
#
# Воспитатель просит сделать программу,
# которая по имени ребенка и номеру его шкафчика формирует «красивую» карточку для личного дела.
#
# Формат ввода
# В первой строке записано имя ребенка.
# Во второй строке записан номер шкафчика.
#
# Формат вывода
# Карточка в виде:
# Группа №<номер группы>.
# <номер ребёнка в списке>. <имя ребенка>.
# Шкафчик: <номер шкафчика>.
# Кроватка: <номер кроватки>.

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
