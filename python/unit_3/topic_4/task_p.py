# Расклад таков...

# Виталий любит играть в карты. Он решил выяснить, какие есть вариации
# вытащить из колоды определённые тройки карт. Напишите программу,
# которая выводит список вариантов согласно требованиям.

# Формат ввода
# В первой строке записана масть, которая должна присутствовать в тройке.
# Во второй строке записан достоинство, которого не должно быть в тройке.

# Формат вывода
# Выведите на экран первые 10 получившихся троек.
# Карты в каждой комбинации должны быть отсортированы
# лексикографически (по строке названия карты). Карты комбинации
# выводятся через запятую с пробелом после неё.
# Комбинации между собой также должны быть отсортированы в
# лексикографическом порядке по строке, представляющей комбинацию целиком.

# Примечание
# Обратите внимание: валет-дама-король-туз лексикографически упорядочены.
# Но «10 ...» лексикографически младше, чем «2 ...», а бубны младше, чем пики.

from itertools import product, permutations

suits = ['пик', 'треф', 'бубен', 'червей']
ranks = [str(n) for n in range(2, 11)] + ['валет', 'дама', 'король', 'туз']

must = input()
ranks.remove(input())
prev = input()

cards = [f'{rank} {suit}' for rank, suit in product(ranks, suits)]
combos = [combo for combo in permutations(cards, 3) if must[:3] in str(combo)]

print('\n'.join(', '.join(combo) for combo in sorted(combos)[:10]))
