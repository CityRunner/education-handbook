# Кто быстрее на этот раз?

# Вновь велогонщики собрались узнать, кто из них быстрее. Им предстоит
# пройти трассу длиной 43872м, и нам нужно вновь определить победителя.

# На этот раз нам известны средние скорости трёх фаворитов — Пети, Васи и
# Толи. Кто из них пришёл к финишу первым?

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Имя победителя гонки.

# Примечание
# Гарантируется, что победителем стал только один.


speed_p = speed_v = speed_t = int()

while speed_p <= 0 or speed_v <= 0 or speed_t <= 0:
    speed_p = int(input())
    speed_v = int(input())
    speed_t = int(input())

if speed_p > speed_v and speed_p > speed_t:
    winner = "Петя"
elif speed_v > speed_t:
    winner = "Вася"
else:
    winner = "Толя"

print(winner)
