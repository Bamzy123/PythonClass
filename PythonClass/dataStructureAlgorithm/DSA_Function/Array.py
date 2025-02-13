class Array:
    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.my_list = []

    def isEmpty(self):
        return len(self.my_list) == 0

    def isFull(self) -> bool:
        return len(self.my_list) == self.capacity

    def append(self, element) -> bool:
        self.my_list.append(element)
        self.size += 1
        return self.isFull()

    def remove(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
            self.size -= 1
        else:
            raise TypeError("Element not found in the list")

    def pop(self, index):
        if index < 0 or index >= len(self.my_list):
            return False
        else:
            self.size -= 1
            return self.my_list.pop(index)

    def insert(self, index, value) -> bool:
        if index < 0 or index > len(self.my_list):
            return False
        else:
            self.my_list.insert(index, value)
            return True