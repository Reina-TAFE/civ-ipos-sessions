class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0
    
my_queue = Queue()

# enqueue tests
my_queue.enqueue(1)
my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(74)

# dequeue tests
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

# peek tests
print(my_queue.peek())