"""
RLE наоборот

Вашему решению будет предоставлен список кортежей rle с символами и количеством их повторений.

Напишите выражение для генерации строки, из которой был получен данный список.

Примечание:
    В решении не должно быть ничего, кроме выражения.

Example 1:
    Input:
        rle = [('a', 2), ('b', 3), ('c', 1)]
    Output:
        'aabbbc'

Example 2:
    Input:
        rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
    Output:
        '100500'
"""

rle = [('a', 2), ('b', 3), ('c', 1)]
print(''.join([letter * count for letter, count in rle]))

# Expression:
# ''.join([letter * count for letter, count in rle])
