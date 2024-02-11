input_binary = 0
input_decimal = 0

while True:
    input_binary = str(input())
    input_decimal = int(input())
    for i in input_binary:
        if i in "01":
            input_is_binary = True
        else:
            input_is_binary = False
            break
    if input_is_binary and input_decimal >= 100:
        break

result = input_decimal - int(input_binary, 2)
print(result)
