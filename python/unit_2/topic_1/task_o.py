# В ожидании доставки

# Сегодня в N часов M минут хозяин магазина заказал доставку нового товара.
# Оператор сказал, что продукты доставят через T минут. Сколько будет времени
# на электронных часах, когда привезут долгожданные продукты?

# Формат ввода
# В первой строке записано натуральное число N (0≤N<24).
# Во второй строке записано натуральное число M (0≤M<60).
# В третьей строке записано натуральное число T (30≤T<10^9).

# Формат вывода
# Одна строка, представляющая циферблат электронных часов.


N = int(input())
M = int(input())
T = int(input())

minutes = (M + T) % 60
hours = (N + (M + T) // 60) % 24

print(f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}')
