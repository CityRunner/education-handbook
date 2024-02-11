red = 0
green = 0
blue = 0

while red <= 0 or green <= 0 or blue <= 0:
    red = int(input())
    green = int(input())
    blue = int(input())

next_is_green = red + blue + 1

print(next_is_green)
