# Привет, всем!

# Но вообще, хорошо бы узнать имя собеседника, а уже потом его приветствовать.

# Напишите диалоговую программу, которая сначала познакомится со своим
# пользователем, а затем поздоровается с ним.

# Формат ввода
# Одна строка — имя пользователя программы.

# Формат вывода:
# В первой строке написан вопрос: «Как Вас зовут?»
# Во второй строке — приветствие пользователя: «Привет, %username%».


username = None

while not username:
    username = input(f'Как Вас зовут?\n')

print(f'Привет, {username}')
