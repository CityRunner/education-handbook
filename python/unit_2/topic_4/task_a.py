# Таблица умножения

# Местная фабрика канцелярских товаров заказала у вас программу, которая
# генерирует таблицы умножения. Давайте поддержим локального производителя!

# Формат ввода
# Вводится одно натуральное число — требуемый размер таблицы.

# Формат вывода
# Таблица умножения заданного размера.



for string_value in range(1, size := int(input()) + 1):
    string = ''
    for column_value in range(1, size):
        string += f'{string_value * column_value} '
    print(string)


# for string_value in range(1, size := int(input()) + 1):
#     string = ''
#     for column_value in range(1, size):
#         if (result := string_value *
#             column_value) < 10 and column_value > 1:
#             result = ' ' + str(result)
#         string += f'{result} '
#     print(string)
