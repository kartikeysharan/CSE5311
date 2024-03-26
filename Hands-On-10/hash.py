class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

class HashTable:
    def __init__(self, initial_capacity=8, load_factor=0.75):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = load_factor
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]

    def hash_function(self, key):
        # Multiplication and division hash function
        return ((key * 2654435761) % 2**32) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        current = bucket.head

        # Check if key already exists, if so, update its value
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        bucket.append(key, value)
        self.size += 1
        if self.size >= self.capacity * self.load_factor:
            self._resize(2 * self.capacity)

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current:
            if current.key == key:
                bucket.remove(current)
                self.size -= 1
                if self.size <= self.capacity // 4:
                    self._resize(self.capacity // 2)
                return
            current = current.next

    def _resize(self, new_capacity):
        new_buckets = [DoublyLinkedList() for _ in range(new_capacity)]

        for bucket in self.buckets:
            current = bucket.head
            while current:
                index = self.hash_function(current.key)
                new_buckets[index].append(current.key, current.value)
                current = current.next

        self.capacity = new_capacity
        self.buckets = new_buckets
