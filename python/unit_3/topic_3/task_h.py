# Аббревиатура

# Вашему решению предоставлена строка string.
# Напишите выражение для генерации строки, представляющей собой
# аббревиатуру заданной.

# Примечание
# В решении не должно быть ничего, кроме выражения.

print('Enter words divided by a single space (e.g., "открытое акционерное общество")')
string = input('string = ')
print(''.join([word[0].upper() for word in string.split()]))

# Expression:
# ''.join([word[0].upper() for word in string.split()])
