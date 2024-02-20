# НОД 2.0

# В одном из местных НИИ часто требуется находить наибольший общий делитель
# (НОД) нескольких чисел. Вам уже доверяют, так что вновь пришли с этой задачей.

# Формат ввода
# В первой строке записано одно число N — количество данных. В каждой из
# последующих N строк записано по одному натуральному числу.

# Формат вывода
# Требуется вывести одно натуральное число — НОД всех данных чисел (кроме N).

# Примечание
# Самый распространённый способ поиска НОД — Алгоритм Евклида.


def is_prime(input_number):
    if (current_number := input_number) > 1:
        for divider in range(2, int(current_number ** 0.5) + 1):
            if current_number % divider == 0:
                return False
    else:
        return False
    return True


def prime_dividers(number):
    dividers = []
    current_divider = 2
    if number > 1 and not is_prime(number):
        while not is_prime(number):
            if number % current_divider == 0:
                number = int(number / current_divider)
                dividers.append(current_divider)
            else:
                while not is_prime(current_divider := current_divider + 1):
                    pass
        dividers.append(number)
    else:
        dividers.append(number)
    return dividers


flag = True
result = 1
p_lists = list()

for i in range(count := int(input())):
    number = int(input())
    p_lists.append(list(set(prime_dividers(number))))
# print(p_lists)

for p_list in range(len(p_lists) - 1):
    for p_current in range(len(p_lists[p_list])):
        for p_next in range(len(p_lists[p_list + 1])):
            if p_lists[p_list][p_current] == p_lists[p_list + 1][p_next]:
                # print(f'''
                #       p_lists[{p_list}][{p_current}] ==
                #       p_lists[{p_list+1}][{p_next}]
                #     ''')
                p_lists[p_list + 1][p_next] = 0
                result *= p_lists[p_list][p_current]

print(result)





