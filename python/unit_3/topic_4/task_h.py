# Меню питания 2.0

# В детском саду ежедневно подают новую кашу на завтрак.
# Напишите программу, которая строит расписание каш на ближайшие дни.

# Формат ввода
# Вводится натуральное число M — количество каш в меню. В каждой из
# последующих M строк записано одно название каши. В конце передается
# натуральное число N — количество дней.

# Формат вывода
# Вывести список каш в порядке подачи.

# Примечание
# Советуем изучить документацию на функцию itertools.islice, которая
# реализует срезы на основе итераторов.

# from itertools import islice, repeat
#
# porridges = [input() for _ in range(int(input()))]
# days = int(input())
#
# porridge_by_day = porridges * (days // len(porridges))
# for porridge in islice(porridges, days % len(porridges)):
#     porridge_by_day.append(porridge)
# print(porridge_by_day)
# print("".join([str(porridporridgesge) for porridge in porridge_by_day]))



from itertools import islice, repeat, cycle

porridges = [input() for _ in range(int(input()))]
print('\n'.join(islice(cycle(porridges), int(input()))))

