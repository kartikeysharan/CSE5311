class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def size(self):
        return len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        while True:
            min_index = i
            left = self.left_child(i)
            right = self.right_child(i)

            if left < self.size() and self.heap[left] < self.heap[min_index]:
                min_index = left

            if right < self.size() and self.heap[right] < self.heap[min_index]:
                min_index = right

            if min_index != i:
                self.swap(i, min_index)
                i = min_index
            else:
                break

    def build_min_heap(self, array):
        self.heap = array[:]
        for i in range(self.size() // 2, -1, -1):
            self.heapify_down(i)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(self.size() - 1)

    def pop(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

# Creating a MinHeap object
min_heap = MinHeap()

# Building a min heap from an array
min_heap.build_min_heap([4, 2, 7, 1, 9, 5])

# Printing the heap
print("Initial Min Heap:", min_heap.heap)

# Inserting an element into the heap
min_heap.insert(3)
print("Min Heap after insertion of 3:", min_heap.heap)

# Popping the minimum element from the heap
print("Popped Element:", min_heap.pop())  # Output: 1
print("Min Heap after popping:", min_heap.heap)

# Building a min heap from an array
min_heap.build_min_heap([4.5, 2.7, 7.2, 1.9, 9.5, 5.3])

# Printing the heap
print("Initial Min Heap:", min_heap.heap)

# Inserting an element into the heap
min_heap.insert(3.8)
print("Min Heap after insertion of 3.8:", min_heap.heap)

# Popping the minimum element from the heap
print("Popped Element:", min_heap.pop())  # Output: 1
print("Min Heap after popping:", min_heap.heap)
