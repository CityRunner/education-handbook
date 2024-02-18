# Красота спасёт мир

# Одно из древних поверий гласит, что трёхзначное число красиво, если сумма его
# минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.
# Напишите систему определяющую красоту числа.

# Формат ввода
# Одно трёхзначное число

# Формат вывода
# YES — если число красивое, иначе — NO


while (number := int(input())) not in range(100, 1000):
    pass

digit_pos = []

digit_pos.append(number // 1 % 10)
digit_pos.append(number // 10 % 10)
digit_pos.append(number // 100 % 10)

digit_sort = []

while digit_pos and len(digit_sort) < 2:
    digit_max = 0
    digit_id = 0
    for index in range(len(digit_pos)):
        if digit_pos[index] >= digit_max:
            digit_max = digit_pos[index]
            digit_id = index
    digit_sort.append(digit_pos[digit_id])
    digit_pos.pop(digit_id)
digit_sort.append(digit_pos[0])

if (digit_sort[0] + digit_sort[2]) == digit_sort[1] * 2:
    print("YES")
else:
    print("NO")
