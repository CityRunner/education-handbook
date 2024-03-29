# Автоматизация безопасности

# Группа исследователей собирается высадиться на остров невероятно ровной
# формы, но разведка при помощи спутника выяснила, что на острове есть зона
# зыбучих песков.

# Для повышения безопасности экспедиции было решено разработать систему
# оповещения, которая предупредит исследователей об опасности. А для
# снижения расходов на производство было решено заказать программное
# обеспечение.

# Напишите программу, которая по координатам исследователя, будет сообщать
# о безопасности в этой точке.

# Формат ввода
# Два рациональных числа — координаты исследователя.

# Формат вывода
# Одно из сообщений:
#     Опасность! Покиньте зону как можно скорее!
#     Зона безопасна. Продолжайте работу.
#     Вы вышли в море и рискуете быть съеденным акулой!


safe_x = safe_y = 0
safe_r = 10
circ_x = circ_y = 0
circ_r = 5
msg = {'sea': 'Вы вышли в море и рискуете быть съеденным акулой!',
       'danger': 'Опасность! Покиньте зону как можно скорее!',
       'safe': 'Зона безопасна. Продолжайте работу.'}

x = float(input())
y = float(input())

if (x - safe_x) ** 2 + (y - safe_y) ** 2 <= safe_r ** 2:
    if y < 0:
        if (x + 7) * (x - 5) / 4 <= y:
            print(msg['danger'])
        else:
            print(msg['safe'])
    else:
        if x >= 0:
            if (x - circ_x) ** 2 + (y - circ_y) ** 2 <= circ_r ** 2:
                print(msg['danger'])
            else:
                print(msg['safe'])
        else:
            if y <= 5 and y <= ((5 * x) + 35) / 3:
                print(msg['danger'])
            else:
                print(msg['safe'])
else:
    print(msg['sea'])
