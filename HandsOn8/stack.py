class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = -1
        self.stack = [None] * max_size

    # Prints the stack
    def print_stack(self):
        print("Print Stack: \t" + str(self.stack[:self.top + 1]))

    # Check if the stack is empty
    def stack_empty(self):
        return self.top == -1

    # Push element to stack - as long as the stack is not at the max size
    def push(self, x):
        print("Push Element: " + str(x))
        if self.top == self.max_size - 1:
            print("ERROR: Overflow")
            return
        self.top += 1
        self.stack[self.top] = x

    # Removes and returns the element from the top of the stack
    def pop(self):
        if self.stack_empty():
            print("ERROR: Underflow")
            return None
        else:
            popped_element = self.stack[self.top]
            self.top -= 1
            return popped_element

# Example usage
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)  # Overflow
stack.print_stack()
print("Popped Element:", stack.pop())
stack.print_stack()
