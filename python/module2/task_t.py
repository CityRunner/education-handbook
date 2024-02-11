# Мухи отдельно, котлеты отдельно
#
# Вернёмся в магазин, хозяин которого уже привык полагаться на всемогущую автоматизацию.
# Помогите ему разобраться с одной проблемой. Далее его история:
# «Пару дней назад я купил две партии котлет и по случайности высыпал их на один прилавок.
# Общий вес котлет составил NN килограмм, а ценник — MM рублей за килограмм.
# Сегодня я обнаружил, что накладные на эти виды котлет потерялись,
# но я помню, что первый вид котлет стоил K1K1​ рублей за килограмм, а второй — K2K2​.
# Помогите мне вспомнить вес каждой партии котлет, чтобы поставить их на учёт.
#
# Формат ввода
# В первой строке записано натуральное число NN
# Во второй строке — натуральное число MM
# В третьей строке — натуральное число K1K1​
# В четвёртой строке — натуральное число K2K2​
# Причём доподлинно известно, что второй вид котлет стоит меньше, чем первый.
#
# Формат вывода
# Два натуральных числа, записанных через пробел — вес обеих партий котлет.

N = M = K1 = K2 = N1 = N2 = int()

while N <= 0 or M <= 0 or K1 <= 0 or K2 <= 0 or K2 > K1:
    N = int(input())
    M = int(input())
    K1 = int(input())
    K2 = int(input())

# N = N1 + N2
# N1 = N - N2
# N2 = N - N1
# K1 * N1 + K2 * N2 = N * M
# K1 * N1 + K2 * N - K2 * N1 = N * M
# K1 * N1 - K2 * N1 = N * M - K2 * N
# N1 * (K1 - K2) = N * M - K2 * N

N1 = int((N * M - K2 * N) / (K1 - K2))
N2 = N - N1

print(N1, N2)
