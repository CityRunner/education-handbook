# Мы делили апельсин 2.0

# Аня, Боря и Вова решили съесть апельсин.
# Подскажите ребятам, как им его разделить.
# Разработайте программу, которая выводит все возможные способы
# разделки апельсина.

# Формат ввода
# В единственной строке записано количество долек апельсина (N).

# Формат вывода
# Таблица вариантов разделения апельсина.

# Примечания
# Каждому ребёнку должна достаться хотя бы одна долька апельсина.
# Ни одной дольки не должно остаться.
# Выводить варианты в порядке увеличения количества долек у Ани,
# следом Бори и затем Вовы.
# Для удобства сведите задачу к разделению долек между двумя ребятами,
# а третьему отдайте остатки.

from itertools import product

nums = list(range(1, num := int(input())))
ways = [[a, b, num - (a + b)] for a, b in product(nums, nums)
        if num - (a + b) > 0]

print('А', 'Б', 'В')
for slices in ways:
    print(*slices)
