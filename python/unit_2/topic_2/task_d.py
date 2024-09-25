"""
Список победителей

Длина трассы — 43872м, и зрители хотят узнать имя победителя.

Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи.
Помогите подвести итоги гонки.

Формат ввода:
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.
    В третьей — Толи.

Формат вывода:
    Имена победителей в порядке занятых мест.

Пример 1:
    Ввод:
        10
        5
        7
    Вывод:
        1. Петя
        2. Толя
        3. Вася

Пример 2:
    Ввод:
        5
        7
        10
    Вывод:
        1. Толя
        2. Вася
        3. Петя
"""

petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    first = 'Петя'
    if vasya > tolya:
        second, third = 'Вася', 'Толя'
    else:
        second, third = 'Толя', 'Вася'
elif vasya > petya and vasya > tolya:
    first = 'Вася'
    if petya > tolya:
        second, third = 'Петя', 'Толя'
    else:
        second, third = 'Толя', 'Петя'
elif tolya > petya and tolya > vasya:
    first = 'Толя'
    if petya > vasya:
        second, third = 'Петя', 'Вася'
    else:
        second, third = 'Вася', 'Петя'

print(f'1. {first}\n2. {second}\n3. {third}')
