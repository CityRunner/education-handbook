# Новогоднее настроение

# Великий математик Виталий Евгеньевич каждый Новый год проводит на работе.
# Коллеги всегда любили и ценили его, поэтому в этом году решили сделать ему
# сюрприз — украсить кабинет учёного математическими ёлками. Помогите
# математикам и напишите программу, которая по введённому числу строит
# математическую ёлку.

# Формат ввода
# Вводится одно натуральное число — количество чисел в математической ёлке.

# Формат вывода
# Требуемая новогодняя ёлка.


last_number = 0
user_number = int(input())

for line in range(1, user_number + 1):
    output = ''
    for current_number in range(last_number + 1,
                                last_number + line + 1):
        if current_number <= user_number:
            output += f'{current_number} '
            last_number = current_number
    print(output)
    if last_number >= user_number:
        break
