# Детский сад — штаны на лямках

# В продолжение темы детского сада давайте и там что-нибудь автоматизируем.
# За каждым ребёнком закреплён шкафчик и кровать. Номер шкафчика состоит из
# трёх цифр:
#     номер группы в саду;
#     номер кроватки закреплённой за ребёнком;
#     порядковый номер ребенка в списке группы.

# Воспитатель просит сделать программу, которая по имени ребенка и номеру его
# шкафчика формирует «красивую» карточку для личного дела.

# Формат ввода
# В первой строке записано имя ребенка.
# Во второй строке записан номер шкафчика.

# Формат вывода
# Карточка в виде:
# Группа №<номер группы>.
# <номер ребёнка в списке>. <имя ребенка>.
# Шкафчик: <номер шкафчика>.
# Кроватка: <номер кроватки>.


name = input()
locker = int(input())

group = locker // 100
number = locker % 10
bed = locker // 10 % 10

print(f'''Группа №{group}.\n{number}. {name}.
Шкафчик: {locker}.\nКроватка: {bed}.''')
