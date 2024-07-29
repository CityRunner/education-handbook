# Слияние

# Напишите функцию merge, которая принимает два отсортированных
# по возрастанию кортежа целых чисел, а возвращает один из всех
# переданных чисел.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# В этой задаче отключены стандартные сортировки.

def merge(first, second):
    numbers = list(first + second)
    sorted_numbers = []
    while numbers:
        sorted_numbers.append(min(numbers))
        numbers.remove(min(numbers))
    return tuple(sorted_numbers)


# result = merge((1, 2), (3, 4, 5))
# print(result)
