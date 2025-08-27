
class Stack:
    def __init__(self):
        self.stack = [None]
    
    def push(self, item):
        self.stack.append(item)
        return

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]
    
my_stack = Stack()
my_stack.push(1)
my_stack.push(5)
my_stack.push(19)
my_stack.push(54)

print("Popped values")
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

print("\nPeek value")
print(my_stack.peek())