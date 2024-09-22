# Длины всех слов - 2

# Напишите функцию length_stats, которая получает текст, а возвращает объект
# Series со словами в качестве индексов и их длинами в качестве значений.
# Все слова в тексте предварительно переведите в нижний регистр, избавьтесь
# от знаков препинания и цифр, а также отсортируйте в лексикографическом
# порядке.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import pandas as pd


def clean(text):
    words = set()
    for word in text.lower().split():
        alphas = ''.join(filter(str.isalpha, word))
        if alphas:
            words.add(alphas)
    return sorted(words)


def length_stats(text):
    return pd.Series({word: len(word) for word in clean(text)})
