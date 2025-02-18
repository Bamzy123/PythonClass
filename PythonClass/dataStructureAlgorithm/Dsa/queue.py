class MyQueue:
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def add(self, item):
        self._queue.append(item)
        return True

    def elements(self):
        if len(self._queue) >= 3:
            return self._queue[2]
        return None

    def remove(self, item):
        if item in self._queue:
            self._queue.remove(item)

    @property
    def size(self):
        return len(self._queue)

    def is_offer(self):
        return not self.is_empty()

    def poll(self):
        if not self.is_empty():
            return self._queue.pop(0)
        return None