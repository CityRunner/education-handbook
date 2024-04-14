# Однофамильцы — 2

# Вновь поможем сотруднику из отдела кадров выяснить, сколько
# мужчин-однофамильцев работает в организации, но уже немного с иными условиями.

# Формат ввода

# В первой строке указывается количество мужчин — сотрудников организации (N).
# Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.

# Формат вывода

# Список однофамильцев в организации с указанием их количества в алфавитном
# порядке. Если таковых нет — вывести «Однофамильцев нет».


namesakes = {}
for _ in range(int(input())):
    if (name := input()) not in namesakes:
        namesakes[name] = 1
    else:
        namesakes[name] += 1

no_namesakes = True
names = []
for name in namesakes:
    if namesakes[name] > 1:
        names.append(name)
        no_namesakes = False

if no_namesakes:
    print('Однофамильцев нет')
else:
    for name in sorted(names):
        print(f'{name} - {namesakes[name]}')
