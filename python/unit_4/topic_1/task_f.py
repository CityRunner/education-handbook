# Модернизация системы вывода

# Разработайте функцию modern_print, которая принимает
# строку и выводит её, если она не была выведена ранее.

# Примечание
# В решении не должно быть вызовов требуемых функций.

printed = []


def modern_print(string):
    if string not in printed:
        printed.append(string)
        print(string)


# modern_print("Hello!")
# modern_print("Hello!")
# modern_print("How do you do?")
# modern_print("Hello!")
