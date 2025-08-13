"""
Длины всех слов по чётности

В этот раз продумайте функцию length_stats, которая получает текст, а возвращает пару объектов Series со словами в качестве индексов и их длинами в качестве значений.

Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример 1
    Ввод
        odd, even = length_stats('Мама мыла раму')
        print(odd)
        print(even)

    Вывод
        Series([], dtype: int64)
        мама    4
        мыла    4
        раму    4
        dtype: int64

Пример 2
    Ввод
        odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
        print(odd)
        print(even)

    Вывод
        домик    5
        и        1
        лес      3
        dtype: int64
        зверушка    8
        опушка      6
        странный    8
        dtype: int64
"""

import pandas as pd


def clean(text):
    words = set()
    for word in text.lower().split():
        alphas = ''.join(filter(str.isalpha, word))
        if alphas:
            words.add(alphas)
    return sorted(words)


def length_stats(text):
    words = clean(text)
    odd = {word: len(word) for word in words if len(word) % 2}
    even = {word: len(word) for word in words if not len(word) % 2}
    return pd.Series(odd, dtype='int64'), pd.Series(even, dtype='int64')
