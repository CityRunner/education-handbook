"""
Новогоднее настроение 2.0

Коллеги математика вновь хотят порадовать его и сделать математические ёлки,
которые украсят кабинет учёного. Помогите им, написав программу, которая
по введённому числу строит математическую ёлку.

Формат ввода:
    Вводится одно натуральное число — количество чисел в математической ёлке.

Формат вывода:
    Требуемая новогодня ёлка.

Пример 1:
    Ввод:
        14
    Вывод:
         1
        2 3
       4 5 6
      7 8 9 10
    11 12 13 14

Пример 2:
    Ввод:
        6
    Вывод:
        1
       2 3
      4 5 6
"""

num_max = int(input())

num_last = 0
for row in range(1, num_max + 1):
    strng = ''
    col_last = num_last + row
    for col in range(num_last + 1, col_last + 1):
        if col <= num_max:
            strng += f'{col} '
            num_last = col
    width = len(strng)
    if col_last >= num_max:
        break

num_last = 0
for row in range(1, num_max + 1):
    strng = ''
    col_last = num_last + row
    for col in range(num_last + 1, col_last + 1):
        if col <= num_max:
            strng += f'{col} '
            num_last = col
    print(f'{strng: ^{width}}')
    if col_last >= num_max:
        break
