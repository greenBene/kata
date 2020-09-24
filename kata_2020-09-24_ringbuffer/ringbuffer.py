
class RingBuffer():
    content = []
    position = 0
    size = 0
    count = 0


    def __init__(self, size):
        self.size = size
        self.content = [None for _ in range(self.size)]

    def add(self, element):
        if self.count < self.size:
            self.count += 1

        self.position += 1
        self.position %= self.size

        self.content[self.position] = element

    def take(self):
        if self.count <= 0:
            raise Exception('RingBuffer is empty.')

        element = self.content[self.position]

        self.position -= 1
        self.position %= self.size
        self.count -= 1

        return element

    def get_count(self):
        return self.count

    def get_size(self):
        return self.size
