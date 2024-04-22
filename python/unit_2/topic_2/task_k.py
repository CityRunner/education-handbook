# Красота спасёт мир

# Одно из древних поверий гласит, что трёхзначное число красиво, если сумма его
# минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.
# Напишите систему определяющую красоту числа.

# Формат ввода
# Одно трёхзначное число

# Формат вывода
# YES — если число красивое, иначе — NO


num = int(input())
pos = []
pos.append(num // 1 % 10)
pos.append(num // 10 % 10)
pos.append(num // 100 % 10)

char_sort = []

while pos and len(char_sort) < 2:
    char_max = 0
    char_id = 0
    for ind, char in enumerate(pos):
        if char >= char_max:
            char_max = char
            char_id = ind
    char_sort.append(pos[char_id])
    pos.pop(char_id)
char_sort.append(pos[0])

if (char_sort[0] + char_sort[2]) == char_sort[1] * 2:
    print("YES")
else:
    print("NO")
