class setFunction:
    def __init__(self):
        self.set = set()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, name):
        self.set.add(name)
        self.size += 1

    def update(self, name):
        self.set.update(name)
        self.size += 1

    def remove(self, word):
        self.set.remove(word)
        self.size -= 1

    def union(self, word):
        self.set.union(word)
        self.size += 1