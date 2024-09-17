# Чек - 2

# В местном магазине решили добавить анализ данных и каждый чек
# представлять в виде DataFrame.
# Прайс-лист уже сформирован в виде объекта Series, где индексами являются
# названия, а значениями — цены.

# Напишите функцию cheque, которая принимает прайс-лист и список покупок в
# виде неопределённого количества именованных параметров (ключ — название
# товара, значение — количество).

# Функция должна вернуть объект DataFrame со столбцами:
#     наименование продукта (product);
#     цена за единицу (price);
#     количество (number);
#     итоговая цена (cost).

# Строки чека должны быть отсортированы по названию продуктов в
# лексикографическом порядке.

# Примечание
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
