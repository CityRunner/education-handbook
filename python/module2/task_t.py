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
