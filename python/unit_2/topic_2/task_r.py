# Территория зла

# В давние времена считалось, что если какая-то местность является треугольником,
# то в ней заключено страшное зло.

# При этом люди оценивали риск встретить зло по форме этого треугольника:
#     в остроугольном треугольнике вероятность встретить зло крайне мала;
#     в тупоугольном — велика;
#     в прямоугольном — 100%.

# Напишите программу, которая по длине сторон треугольной местности, определяет
# вероятность встретить зло.

# Формат ввода
# Три числа — длины сторон треугольной местности.

# Формат вывода
# Вероятность встретить зло согласно поверью:
#     крайне мала;
#     велика;
#     100%.

def probability(a, b, c):
    if a ** 2 > b ** 2 + c ** 2:
        print('велика')
    elif a ** 2 < b ** 2 + c ** 2:
        print('крайне мала')
    else:
        print('100%')


a = b = c = int()

while a <= 0 or b <= 0 or c <= 0:
    a = int(input())
    b = int(input())
    c = int(input())

if a + b > c and a + c > b and c + b > a:
    if a >= b and a >= c:
        probability(a, b, c)
    elif b >= a and b >= c:
        probability(b, a, c)
    elif c >= a and c >= b:
        probability(c, a, b)
