# Легенды велогонок возвращаются: кто быстрее?
#
# В новом сезоне за первенство в велогонках вновь борются лучшие из лучших.
# Протяжённость заключительной трассы — 43872м,
# и все хотят знать, кто получит золотую медаль.
# Нам известны средние скорости трёх претендентов на победу
# – Пети, Васи и Толи. Кто из них победит?
#
# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.
#
# Формат вывода
# Красивый пьедестал (ширина ступеней 8 символов).

substring = 8 * ' '
places = []
racers = ["  Петя  ", "  Вася  ", "  Толя  "]
speed = [int(), int(), int()]

for index in range(len(speed)):
    while speed[index] <= 0:
        speed[index] = int(input())

while speed and len(places) < 2:
    max_speed = 0
    racer_id = 0
    for index in range(len(speed)):
        if speed[index] >= max_speed:
            max_speed = speed[index]
            racer_id = index
    places.append(racers[racer_id])
    speed.pop(racer_id)
    racers.pop(racer_id)
places.append(racers[0])

print(f"""{substring}{places[0]}{substring}
{places[1]}{substring}{substring}
{substring}{substring}{places[2]}
   II      I      III   """)
