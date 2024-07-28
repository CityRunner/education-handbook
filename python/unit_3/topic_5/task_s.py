# Это будет наш секрет

# Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один из самых
# простых и наиболее широко известных методов шифрования. Он назван в честь
# римского полководца Гая Юлия Цезаря, использовавшего его для секретной
# переписки со своими генералами. Давайте реализуем эту систему шифрования.
# Однако для простоты мы будем сдвигать только латинские символы по кругу.

# Формат ввода
# Вводится размер сдвига для шифрования.
# В файле public.txt содержится текст на английском языке.

# Формат вывода
# В файл private.txt запишите зашифрованный текст.

with open('public.txt', encoding='UTF-8') as file_in:
    text = file_in.read()

shift = int(input()) % 26

output = ''
for char in text:
    if char.isalpha():
        code = ord(char) + shift
        end = 122 if char.islower() else 90
        char = chr(code - 26) if code > end else chr(code)
    output += char

with open('private.txt', 'w', encoding='UTF-8') as file_out:
    file_out.write(output)
