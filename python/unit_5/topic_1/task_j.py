# Стек

# Ещё одной полезной коллекцией является стек, реализующий принцип
# «Последний пришёл – первый ушёл». Его часто представляют как
# стопку карт или магазин пистолета, где приходящие элементы
# закрывают выход уже находящимся в коллекции.

# Реализуйте класс Stack, который не имеет параметров
# инициализации, но поддерживает методы:
#     push(item) — добавить элемент в конец стека;
#     pop() — «вытащить» первый элемент из стека;
#     is_empty() — проверяет стек на пустоту.

# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Stack:
    s = list()

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.s:
            return self.s.pop()

    def is_empty(self):
        if not self.s:
            return True
        else:
            return False


# stack = Stack()
# for item in range(10):
#     stack.push(item)
# while not stack.is_empty():
#     print(stack.pop(), end=" ")
#
# stack = Stack()
# for item in ("Hello,", "world!"):
#     stack.push(item)
# while not stack.is_empty():
#     print(stack.pop())
