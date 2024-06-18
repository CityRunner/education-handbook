# Буквенная статистика

# Вашему решению будет предоставлена строка text.
# Напишите выражение для генерации словаря, который содержит
# информацию о частоте употребления букв в заданной строке.
# При анализе не учитывайте регистр, а ключами словаря сделайте
# использованные в строке буквы в нижнем регистре.

# Примечание
# В решении не должно быть ничего, кроме выражения.

print('Enter words divided by a single space (e.g., "Мама мыла раму!")')
text = input('text = ')
print({letter: text.lower().count(letter) for letter
       in sorted(set(text.lower())) if letter.isalpha()})

# Expression:
# {letter: text.lower().count(letter) for letter in sorted(set(text.lower())) if letter.isalpha()}
