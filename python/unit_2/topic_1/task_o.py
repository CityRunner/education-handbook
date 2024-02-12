# В ожидании доставки
#
# Сегодня в NN часов MM минут хозяин магазина заказал доставку нового товара.
# Оператор сказал, что продукты доставят через TT минут.
# Сколько будет времени на электронных часах, когда привезут долгожданные продукты?
#
# Формат ввода
# В первой строке записано натуральное число NN (0≤N<240≤N<24).
# Во второй строке записано натуральное число MM (0≤M<600≤M<60).
# В третьей строке записано натуральное число TT (30≤T<10930≤T<109).
#
# Формат вывода
# Одна строка, представляющая циферблат электронных часов.

N = 0
M = 0
T = 0

time = {"hours": 0,
        "minutes": 0}

while True:
    N = int(input())
    M = int(input())
    T = int(input())
    if 0 <= N < 24 and 0 <= M < 60 and 30 <= T < 10 ** 9:
        break

time["minutes"] = (M + T) % 60
time["hours"] = (N + (M + T) // 60) % 24

for value in time:
    if time[value] < 10:
        time[value] = "0" + str(time[value])

print(f'{time["hours"]}:{time["minutes"]}')