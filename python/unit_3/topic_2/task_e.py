# Кашееды — 2

# Изменим задачу и напишем программу, которая поможет быстро выяснить, сколько
# детей любят только одну кашу.

# Формат ввода
# В первых двух строках указывается количество детей, любящих манную и овсяную
# каши (N и M). Затем идут N+M строк — перемешанные фамилии детей.
# Гарантируется, что в группе нет однофамильцев.

# Формат вывода
# Количество учеников, которые любят только одну кашу. Если таких не окажется,
# в строке вывода нужно написать «Таких нет».


N, M = int(input()), int(input())
none = 'Таких нет'
NMs = set()

for _ in range(N + M):
    if (name := input()) in NMs:
        NMs.remove(name)
    else:
        NMs.add(name)

if (porridge_eaters := len(NMs)) > 0:
    print(porridge_eaters)
else:
    print(none)
