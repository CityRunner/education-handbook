# RLE наоборот

# Вашему решению будет предоставлен список кортежей tple с символами и
# количеством их повторений.
# Напишите выражение для генерации строки, из которой был получен
# данный список.

# Примечание
# В решении не должно быть ничего, кроме выражения.

print('Enter value couples divided by a single space (e.g., "a2 b3 c1")')
rle = [(sym, int(num)) for sym, num in list(input('rle = ').split())]
print(''.join([letter * count for letter, count in rle]))

# Expression:
# ''.join([letter * count for letter, count in rle])
