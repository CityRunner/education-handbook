# Обработка ошибок

# Вашему решению будет предоставлена функция func, которая не имеет
# параметров и результата. Однако во время её исполнения может
# произойти одна из ошибок: ValueError, TypeError или SystemError.

# Вызовите её, обработайте ошибку и выведите её название. Если ошибка
# не произойдёт, выведите сообщение "No Exceptions".

try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except SystemError:
    print('SystemError')
else:
    print('No Exceptions')
