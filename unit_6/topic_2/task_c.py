"""
Чек - 2

В местном магазине решили добавить анализ данных и каждый чек представлять в виде DataFrame.
Прайс-лист уже сформирован в виде объекта Series, где индексами являются названия, а значениями — цены.

Напишите функцию, cheque, которая принимает прайс-лист и список покупок в виде неопределённого количества именованных параметров (ключ — название товара, значение — количество).

Функция должна вернуть объект DataFrame со столбцами:
    наименование продукта (product);
    цена за единицу (price);
    количество (number);
    итоговая цена (cost).

Строки чека должны быть отсортированы по названию продуктов в лексикографическом порядке.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример
    Ввод
        products = ['bread', 'milk', 'soda', 'cream']
        prices = [37, 58, 99, 72]
        price_list = pd.Series(prices, products)
        result = cheque(price_list, soda=3, milk=2, cream=1)
        print(result)

    Вывод
        product  price  number  cost
        0   cream     72       1    72
        1    milk     58       2   116
        2    soda     99       3   297
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
