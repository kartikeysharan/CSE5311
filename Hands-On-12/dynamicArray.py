class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = self.create_array(self.capacity)

    def create_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def resize(self, new_capacity):
        new_array = self.create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def push_back(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("pop from empty array")
        self.size -= 1
        element = self.array[self.size]
        if self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)
        return element

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("index out of range")
        return self.array[index]

    def __len__(self):
        return self.size

    def __str__(self):
        return '[' + ', '.join(str(self.array[i]) for i in range(self.size)) + ']'

