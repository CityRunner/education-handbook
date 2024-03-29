# Ошибка кассового аппарата

# Мы уже помогали магазину с расчётами и формированием чеков, но сегодня
# кассовый аппарат вместо привычных продавцу десятичных чисел начал выдавать
# двоичные. Техподдержка приедет только завтра, а магазин должен продолжать
# работать. Надо помочь.

# Формат ввода
# В первой строке записано десятичное число — общая сумма купленных в магазине
# товаров на данный момент.
# Во второй строке указано двоичное число — сумма за последнюю покупку.

# Формат вывода
# Одно десятичное число — сумма прибыли за день с учётом последней покупки.


input_decimal = 0
input_binary = 0

while True:
    input_decimal = int(input())
    input_binary = str(input())
    for i in input_binary:
        if i in "01":
            input_is_binary = True
        else:
            input_is_binary = False
            break
    if input_decimal >= 0 and input_is_binary:
        break

result = input_decimal + int(input_binary, 2)
print(result)
