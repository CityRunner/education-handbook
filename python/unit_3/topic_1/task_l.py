# Меню питания

# В детском саду ежедневно подают новую кашу на завтрак.
# Каши чередуются в следующем порядке:
#     Манная;
#     Гречневая;
#     Пшённая;
#     Овсяная;
#     Рисовая.
# Напишите программу, которая строит расписание каш на ближайшие дни.

# Формат ввода
# Вводится натуральное число N — количество дней.

# Формат вывода
# Вывести список каш в порядке подачи.

porridges = ('Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая')

days = int(input())
if days == len(porridges):
    for porridge in porridges:
        print(porridge)
elif days < len(porridges):
    for porridge in range(days):
        print(porridges[porridge])
else:
    full_weeks = days // len(porridges)
    for week in range(full_weeks):
        for porridge in porridges:
            print(porridge)
    if (last_week := days % len(porridges)) != 0:
        for porridge in range(last_week):
            print(porridges[porridge])
