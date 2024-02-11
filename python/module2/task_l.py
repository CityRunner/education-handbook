num_1 = None
num_2 = None
while num_1 not in range(1000) or num_2 not in range(1000):
    num_1 = int(input())
    num_2 = int(input())

summ = [0, 1, 2]

summ[0] = str(((num_1 // 100) + (num_2 // 100)) % 10)
summ[1] = str(((num_1 // 10) + (num_2 // 10)) % 10)
summ[2] = str(((num_1 % 10) + (num_2 % 10)) % 10)

result = int(''.join(summ))

print(result)
