# Раз, два, три! Ёлочка, гори!
#
# В детском саду проводят новогодний утренник.
# Со знанием чисел и их порядком у детей пока есть небольшие проблемы,
# но цифру три знают все без исключения.
# Напишите программу, которая зажигает Ёлочку, когда все дети прокричат «Три!»
#
# Формат ввода
# Вводятся крики детей.
#
# Формат вывода
# Выводить «Режим ожидания...», пока дети не прокричат «Три!».
# В конце вывести «Ёлочка, гори!»

while input() != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')
