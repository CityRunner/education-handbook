# Зайка — 3

# В задачнике ко второй лекции мы помогали детям искать зайца.
# На этот раз мы будем искать и считать сразу нескольких зайчат.

# Формат ввода
# Вводятся строки, описывающие придорожную местность.
# В конце поездки вводится «Приехали!»

# Формат вывода
# Количество строк, в которых есть зайка.


count = int()
while (string := input()) != 'Приехали!':
    if 'зайка' in string:
        count += 1
print(count)
