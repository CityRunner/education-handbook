# Список победителей

# Длина трассы — 43872м, и зрители хотят узнать имя победителя.

# Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. Помогите
# подвести итоги гонки.

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Имена победителей в порядке занятых мест.


places = []
racers = ["Петя", "Вася", "Толя"]
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

for index in range(len(places)):
    print(f"{index+1}. {places[index]}")
