# Новогоднее настроение 2.0

# Коллеги математика вновь хотят порадовать его и сделать математические ёлки,
# которые украсят кабинет учёного. Помогите им, написав программу, которая по
# введённому числу строит математическую ёлку.

# Формат ввода
# Вводится одно натуральное число — количество чисел в математической ёлке.

# Формат вывода
# Требуемая новогодня ёлка.

# Примечание
# Не забывайте про существование f-строк.


user_number = int(input())
rows = 0
counter = user_number
while counter > 0:
    rows += 1
    counter -= rows

strings = []
string_length = 0
current_number = 0

for row in range(rows):
    string = ''
    for col in range(row + 1):
        current_number += 1
        if current_number <= user_number:
            string += str(current_number) + ' '
    if len(string) >= string_length:
        string_length = len(string)
    strings.append(string)

for string in strings:
    print(f'{string: ^{string_length}}')
