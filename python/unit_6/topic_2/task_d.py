# Акция

# Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:
# При покупке больше двух товаров — скидка 50%
# мелкий шрифт: скидка распространяется только на товары купленные в количестве
# более двух штук.

# Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую
# новый с учётом акции.

# Примечание
# Не удаляйте функцию cheque, она потребуется для тестирования.
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

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
