# Прятки

# Стеганография — способ передачи или хранения информации с учётом
# сохранения в тайне самого факта такой передачи (хранения). В отличие от
# криптографии, которая скрывает содержимое тайного сообщения,
# стеганография скрывает сам факт его существования. Как правило,
# сообщение будет выглядеть как что-либо иное, например, как изображение,
# статья, список покупок, письмо или судоку. Стеганографию обычно
# используют совместно с методами криптографии, таким образом, дополняя
# её. Нам был дан файл со скрытым текстом. И было сообщено, что для
# выделения полезной информации, нужно из каждого кода символа в тексте
# «выдернуть» младший байт. Это и будет код символа полезной информации.
# Однако есть одно «но». Если код символа меньше 128 — это и есть полезная
# информация. Разработайте программу, которая из текстового файла
# выделяет полезную информацию.

# Формат ввода
# В файле secret.txt хранится текст.

# Формат вывода
# Выведите спрятанное сообщение.

# Примечание
# Для манипуляции кодами символов изучите работу функций chr и ord.

with open('secret.txt', encoding='UTF-8') as file_in:
    secret = file_in.read()
    print(''.join(chr(ord(char) & 255) for char in secret))
