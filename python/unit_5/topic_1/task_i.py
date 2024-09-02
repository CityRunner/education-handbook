# Очередь

# В программировании существует потребность не только в изученных
# нами коллекциях. Одна из таких — очередь. Она реализует подход к
# хранению данных по принципу «Первый вошёл – первый ушел».
# Реализуйте класс Queue, который не имеет параметров инициализации,
# но поддерживает методы:
#     push(item) — добавить элемент в конец очереди;
#     pop() — «вытащить» первый элемент из очереди;
#     is_empty() — проверяет очередь на пустоту.

# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Queue:
    q = list()

    def push(self, item):
        self.q.append(item)

    def pop(self):
        if self.q:
            return self.q.pop(0)

    def is_empty(self):
        if not self.q:
            return True
        else:
            return False


# queue = Queue()
# for item in range(10):
#     print(item)
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop(), end=" ")
#
# queue = Queue()
# for item in ("Hello,", "world!"):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop())
