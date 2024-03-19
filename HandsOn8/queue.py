class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.front = 0
        self.rear = -1
        self.size = 0
        self.queue = [None] * max_size

    def print_queue(self):
        print("Print Queue: \t", end="")
        if self.is_empty():
            print("Empty")
        else:
            for i in range(self.size):
                print(self.queue[(self.front + i) % self.max_size], end=" ")
            print()

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print("ERROR: Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("ERROR: Queue Underflow")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

# Example usage
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # Overflow
queue.print_queue()
print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())
queue.print_queue()
