# Слияние с проверкой

# Когда-то вы уже писали функцию merge, которая производит слияние двух
# отсортированных кортежей.

# Давай-те её немного переработаем.

# Введём систему проверок:
#     если один из параметров не является итерируемым объектом, то
#     вызовите исключение StopIteration;
#     если значения входных параметров содержат «неоднородные» данные,
#     то вызовите исключение TypeError;
#     если один из параметров не отсортирован, то вызовите исключение
#     ValueError.

# Проверки следует проводить в указанном порядке.
# Если параметры прошли все проверки, верните итерируемый объект,
# являющийся слиянием двух переданных.

# Примечание
# В решении не должно быть вызовов требуемых функций.

def merge(tuple_1, tuple_2):
    check(tuple_1, tuple_2)
    list_1 = list(tuple_1)
    list_2 = list(tuple_2)
    result = []
    while list_1 and list_2:
        if list_1[0] > list_2[0]:
            result.append(list_2.pop(0))
        else:
            result.append(list_1.pop(0))
    result.extend(list_1 + list_2)
    return tuple(result)


def check(t_1, t_2):
    for t in [t_1, t_2]:
        try:
            iter(t)
        except TypeError:
            raise StopIteration
    t_list = list(t_1) + list(t_2)
    if not all(type(el) is type(t_list[0]) for el in t_list):
        raise TypeError
    if list(t_1) != sorted(t_1) or list(t_2) != sorted(t_2):
        raise ValueError
