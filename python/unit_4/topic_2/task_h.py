# Длинная сортировка

# Напишите lambda выражение для сортировки списка слов сначала
# по длине, а затем по алфавиту без учёта регистра.

# Примечание
# В решении не должно быть ничего, кроме выражения.

string = input()
print(sorted(string.split(), key=lambda line: (len(line.lower()), line.lower())))

# Expression
# lambda line: (len(line.lower()), line.lower())
