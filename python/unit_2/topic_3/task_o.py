# Зайка - 4

# Давайте вновь поиграем с детьми и поможем им найти заек.

# Формат ввода
# В первой строке записано натуральное число NN — количество выделенных
# придорожных местностей. В каждой из NN последующих строках — описание
# придорожной местности.

# Формат вывода
# Количество строк, в которых есть зайка.


count = 0
for repeat in range(int(input())):
    if 'зайка' in input():
        count += 1
print(count)
