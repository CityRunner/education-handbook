A = B = C = int()

while A <= 0 or B <= 0 or C <= 0:
    A = int(input())
    B = int(input())
    C = int(input())

path = abs(B - A)
result = round(path / C, 2)

print(result)
