# Длины всех слов

# Вашему решению будет предоставлена строка sentence слов, разделённых
# пробелами.
# Напишите списочное выражения для генерации списка длин слов.

# Примечание
# В решении не должно быть ничего, кроме списочного выражения.

print('Enter words divided by a single space (e.g., "Мама мыла раму")')
sentence = input('sentence = ')
print([len(word) for word in sentence.split()])

# Expression:
# [len(word) for word in sentence.split()]
