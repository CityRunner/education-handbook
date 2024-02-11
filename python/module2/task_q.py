input_decimal = 0
input_binary = 0

while True:
    input_decimal = int(input())
    input_binary = str(input())
    for i in input_binary:
        if i in "01":
            input_is_binary = True
        else:
            input_is_binary = False
            break
    if input_decimal >= 0 and input_is_binary:
        break

result = input_decimal + int(input_binary, 2)
print(result)
