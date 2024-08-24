# Шашки

# Шашки очень занимательная игра, которую достаточно легко моделировать.
# Правила подразумевают наличие двух классов: игральная доска и
# шашка. Однако мы немного упростим себе задачу и вместо шашки будем
# манипулировать клетками, которые могут находиться в трех состояниях:
# пустая, белая шашка и чёрная шашка.
# Разработайте два класса: Checkers и Cell.

# Объекты класса Checkers при инициализации строят игральную доску со
# стандартным распределением клеток и должны обладать методами:
#     move(f, t) — перемещает шашку из позиции f в позицию t;
#     get_cell(p) — возвращает объект «клетка» в позиции p.

# Объекты класса Cell при инициализации принимают одно из трех
# состояний: W — белая шашка, B — чёрная шашка, X — пустая клетка,
# а также обладают методом status() возвращающим заложенное в ней
# состояние.

# Координаты клеток описываются строками вида PQ, где:
#     P — столбец игральной доски, одна из заглавных латинских букв:
#     ABCDEFGH;
#     Q — строка игральной доски, одна из цифр: 12345678.

# Будем считать, что пользователь всегда ходит правильно и контролировать
# возможность хода не требуется.

# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Checkers:

    def __init__(self):
        chkrs = list('WX' * 4 +
                     'XW' * 4 +
                     'WX' * 4 +
                     'X' * 16 +
                     'XB' * 4 +
                     'BX' * 4 +
                     'XB' * 4)
        self.board = [[Cell(chkrs[col * 8 + row]) for col in range(8)]
                      for row in range(8)]

    def get_coord(self, c):
        col = list('ABCDEFGH').index(c[0])
        row = list('12345678').index(c[1])
        return col, row

    def move(self, f, t):
        col, row = self.get_coord(t)
        self.board[col][row] = self.get_cell(f)
        col, row = self.get_coord(f)
        self.board[col][row] = Cell()

    def get_cell(self, p):
        col, row = self.get_coord(p)
        return self.board[col][row]


class Cell:

    def __init__(self, state='X'):
        self.state = state

    def status(self):
        return self.state

# checkers = Checkers()
# for row in '87654321':
#     for col in 'ABCDEFGH':
#         print(checkers.get_cell(col + row).status(), end='')
#     print()

# checkers = Checkers()
# checkers.move('C3', 'D4')
# checkers.move('H6', 'G5')
# for row in '87654321':
#     for col in 'ABCDEFGH':
#         print(checkers.get_cell(col + row).status(), end='')
#     print()
