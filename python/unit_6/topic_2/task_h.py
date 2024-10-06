"""
Обновление журнала

Продолжим обрабатывать DataFrame из прошлых задач.

Напишите функцию update, которая добавляет к данным столбец average, содержащий среднюю оценку ученика, а также сортирует данные по убыванию этого столбца, а при равенстве средних — по имени лексикографически.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.

Пример
    Ввод
        columns = ['name', 'maths', 'physics', 'computer science']
        data = {
            'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
            'maths': [5, 4, 5, 2, 4],
            'physics': [4, 4, 4, 5, 5],
            'computer science': [5, 2, 5, 4, 3]
        }
        journal = pd.DataFrame(data, columns=columns)
        filtered = update(journal)
        print(journal)
        print(filtered)

    Вывод
            name  maths  physics  computer science
        0    Иванов      5        4                 5
        1    Петров      4        4                 2
        2   Сидоров      5        4                 5
        3  Васечкин      2        5                 4
        4  Николаев      4        5                 3
            name  maths  physics  computer science   average
        0    Иванов      5        4                 5  4.666667
        2   Сидоров      5        4                 5  4.666667
        4  Николаев      4        5                 3  4.000000
        3  Васечкин      2        5                 4  3.666667
        1    Петров      4        4                 2  3.333333
"""

import pandas as pd


def update(journal):
    avg = [journal.values[row, 1:].sum() / 3 for row in range(len(journal))]
    journal = journal.assign(average=avg)
    return journal.sort_values(['average', 'name'], ascending=[False, True])
