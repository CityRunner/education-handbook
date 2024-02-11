sweets = 0
childs = 0
while sweets <= 0 or childs <= 0:
    childs = int(input())
    sweets = int(input())
equal = sweets // childs
left = sweets % childs
print(equal)
print(left)
