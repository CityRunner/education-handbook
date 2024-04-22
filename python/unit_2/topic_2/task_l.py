# Музыкальный инструмент

# Есть много музыкальных инструментов, но Вася обожает треугольник.
# У него завалялось немного алюминиевых трубочек разной длины, и он задаётся
# вопросом, а можно ли из них сделать любимый музыкальный инструмент.

# Формат ввода
# Три числа — длины трубочек, каждое с новой строки.

# Формат вывода
# YES — если Васе удастся создать музыкальный треугольник, иначе — NO

# Примечание
# Обратите внимание, что в треугольнике любая сторона меньше суммы двух других.


t1 = int(input())
t2 = int(input())
t3 = int(input())

cases = [t1 < t2 + t3,
         t2 < t1 + t3,
         t3 < t1 + t2]

if all(cases):
    print("YES")
else:
    print("NO")
