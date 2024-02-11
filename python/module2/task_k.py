numbers = None
while numbers not in range(1000, 10000):
    numbers = int(input())
letters = str(numbers)
srebmun = int(letters[1:2] + letters[0:1] + letters[3:4] + letters[2:3])
print(srebmun)
