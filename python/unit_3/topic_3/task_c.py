"""
Длины всех слов

Вашему решению будет предоставлена строка sentence слов, разделённых пробелами.

Напишите списочное выражение для генерации списка длин слов.

Примечание:
    В решении не должно быть ничего, кроме списочного выражения.

Example 1:
    Input:
        sentence = 'Мама мыла раму'
    Output:
        [4, 4, 4]

Example 2:
    Input:
        sentence = 'Ехали медведи на велосипеде'
    Output:
        [5, 7, 2, 10]
"""

sentence = 'Мама мыла раму'
print([len(word) for word in sentence.split()])

# Expression:
# [len(word) for word in sentence.split()]
