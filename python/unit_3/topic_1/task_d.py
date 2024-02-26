# Очистка данных

# Местный провайдер собирает большое количество логов, однако зачастую файлы
# с отчётами приходят в негодность. Самые частые проблемы — ошибки вида ## и
# @@@. Напишите программу, которая избавляется от:
#     Двух символов # в начале информационных сообщений;
#     Строк, заканчивающихся тремя символами @.

# Формат ввода
# Вводятся строки отчёта. Признаком завершения ввода считается пустая строка.

# Формат вывода
# Очищенные данные.


output = []

while (string := input()) != '':

    cleared_string = ''
    flag = False

    if string[-1] == '@' and len(string) >= 3:
        if string[-2] + string[-3] == '@@':
            flag = True

    elif string[0] == "#" and len(string) >= 2:
        if string[1] == "#":
            for letter in range(2, len(string)):
                cleared_string += string[letter]

    if cleared_string != '':
        output.append(cleared_string)
    elif not flag:
        output.append(string)

else:
    for string in output:
        print(string)
