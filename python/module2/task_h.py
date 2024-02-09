repeat = 0
message = None
while repeat <= 0 and not message:
    repeat = int(input())
    message = input()
for count in range(repeat):
    print(f'Я больше никогда не буду писать "{message}"!')
