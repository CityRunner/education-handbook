# Первому игроку приготовиться 2.0

# Во многих играх порядок ходов определяется броском кубика или монетки, а в
# нашей первым ходит тот, чье имя лексикографически меньше. Определите, кто из
# игроков будет ходить первым.

# Формат ввода
# В первой строке записано одно натуральное число NN — количество игроков.
# В каждой из последующих NN строк указано одно имя игрока.

# Формат вывода
# Имя игрока, который будет ходить первым.


players = int(input())
player_one = input()

for count in range(players - 1):
    if (player_two := input()) < player_one:
        player_one = player_two

print(player_one)