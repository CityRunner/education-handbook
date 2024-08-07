# Ключевой секрет

# Вася любит секреты и шифрование. Он часто пользуется шифром на основе
# замен и просит разработать вас функцию, которая позволит ему быстро
# шифровать сообщения.
# Напишите функцию secret_replace(text, **replaces), которая принимает:
#     текст требующий шифрования;
#     именованные аргументы — правила замен, представляющие собой
#     кортежи из одного или нескольких значений.
# Функция должна вернуть зашифрованный текст.

# Примечание
# Ваше решение должно содержать только функции. В решении не должно
# быть вызовов требуемых функций. Обратите внимание, что позиционный
# аргумент требуемой функции не должен иметь однобуквенного имени.


def secret_replace(text, **replaces):
    text = list(text)
    for r_letter, r_symbols in replaces.items():
        s_index = 0
        for letter in text:
            if letter == r_letter:
                text[text.index(letter)] = r_symbols[s_index]
                s_index = 0 if s_index + 1 > len(r_symbols) - 1 else s_index + 1
    return ''.join(text)


# result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
# print(result)
# result = secret_replace(
#     "ABRA-KADABRA",
#     A=("Z", "1", "!"),
#     B=("3",),
#     R=("X", "7"),
#     K=("G", "H"),
#     D=("0", "2"),)
# print(result)
