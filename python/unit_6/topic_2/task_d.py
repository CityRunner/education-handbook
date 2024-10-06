"""
Акция

Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:

При покупке больше двух товаров — скидка 50%

мелкий шрифт: скидка распространяется только на товары купленные в количестве более двух штук

Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую новый с учётом акции.

Примечание
    Не удаляйте функцию cheque, она потребуется для тестирования.

    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример
    Ввод
        products = ['bread', 'milk', 'soda', 'cream']
        prices = [37, 58, 99, 72]
        price_list = pd.Series(prices, products)
        result = cheque(price_list, soda=3, milk=2, cream=1)
        with_discount = discount(result)
        print(result)
        print(with_discount)

    Вывод
        product  price  number  cost
        0   cream     72       1    72
        1    milk     58       2   116
        2    soda     99       3   297
        product  price  number   cost
        0   cream     72       1   72.0
        1    milk     58       2  116.0
        2    soda     99       3  148.5
"""

import pandas as pd


def cheque(price_list, **kwargs):
    products = sorted(kwargs)
    prices = [price_list[product] for product in products]
    numbers = [kwargs[product] for product in products]
    costs = [price * number for price, number in zip(prices, numbers)]
    check = {'product': products,
             'price': prices,
             'number': numbers,
             'cost': costs}
    return pd.DataFrame(check)


def discount(check):
    d_check = check.copy()
    for index, number in enumerate(d_check['number']):
        if number > 2:
            d_check['cost'] = d_check['cost'].astype(float)
            d_check.loc[index, 'cost'] /= 2
    return d_check
