# Простая задача 4.0

# Напомним, что взаимно простыми называются числа, которые не имеют общих
# делителей кроме 1. Напишите программу, которая для каждого переданного
# числа находит список его взаимно простых.

# Формат ввода
# Задана последовательность чисел записанных через точку с запятой (;) и
# пробел.

# Формат вывода
# Список чисел с указанием взаимно простых ему среди переданных. Все числа
# должны быть выведены в порядке возрастания без повторений.
# Строки следует отформатировать по правилу: число - взаимно простое 1,
# взаимно простое 2, ... Если для числа не было найдено ни одного взаимно
# простого, то и выводить его не требуется.


def is_prime(input_num):
    if (current_num := input_num) > 1:
        for div in range(2, int(current_num ** 0.5) + 1):
            if current_num % div == 0:
                return False
    else:
        return False
    return True


def dividers(input_num):
    divs = []
    for div in range(2, input_num + 1):
        if input_num % div == 0:
            divs.append(div)
    return divs


num_list = set()
nums = {}
for num in input().split('; '):
    num_list.add(int(num))
    nums[num] = set()
    if is_prime(int(num)):
        nums[num].add(int(num))
    else:
        nums[num] = nums[num].union(dividers(int(num)))

cmn_primes = {}
for num_1 in nums:
    cmn_primes[num_1] = set()
    for num_2 in nums:
        if len(nums[num_1] & nums[num_2]) == 0:
            cmn_primes[num_1].add(int(num_2))

for num in sorted(list(num_list)):
    primes = ', '.join(str(p) for p in sorted(list(cmn_primes[str(num)])))
    if len(primes) > 0:
        print(f'{num} - {primes}')
