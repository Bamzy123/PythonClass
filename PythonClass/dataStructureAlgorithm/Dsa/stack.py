class Stack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]

    def size(self):
        return len(self._data)