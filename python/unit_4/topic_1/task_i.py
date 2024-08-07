# Простая задача 5.0

# Напишите функцию is_prime, которая принимает натуральное
# число, а возвращает булево значение: True — если переданное
# число простое, а иначе — False.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.


def is_prime(input_num):
    if (current_num := input_num) > 1:
        for div in range(2, int(current_num ** 0.5) + 1):
            if current_num % div == 0:
                return False
    else:
        return False
    return True


# result = is_prime(1001459)
# print(result)
