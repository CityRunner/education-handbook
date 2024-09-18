# Обновление журнала

# Продолжим обрабатывать DataFrame из прошлых задач.
# Напишите функцию update, которая добавляет к данным столбец average,
# содержащий среднюю оценку ученика, а также сортирует данные по убыванию
# этого столбца, а при равенстве средних — по имени лексикографически.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import pandas as pd


def update(journal):
    avg = [journal.values[row, 1:].sum() / 3 for row in range(len(journal))]
    journal = journal.assign(average=avg)
    # return journal.sort_values(by=['average'], ascending=False).sort_values(by=['name'], ascending=False)
    return journal.sort_values(['average', 'name'], ascending=[False, True])
