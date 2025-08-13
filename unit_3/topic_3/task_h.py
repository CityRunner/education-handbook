"""
Аббревиатура

Вашему решению предоставлена строка string.

Напишите выражение для генерации строки, представляющей собой аббревиатуру заданной.

Примечание:
    В решении не должно быть ничего, кроме выражения.

Example 1:
    Input:
        string = 'Российская Федерация'
    Output:
        'РФ'

Example 2:
    Input:
        string = 'открытое акционерное общество'
    Output:
        'ОАО'
"""

string = 'Российская Федерация'
print(''.join([word[0].upper() for word in string.split()]))

# Expression:
# ''.join([word[0].upper() for word in string.split()])
