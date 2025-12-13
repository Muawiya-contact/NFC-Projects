class Queue:
    def __init__(self):
        self.items = []
        self.sum = 0  # To help moving average calculation
    
    def enqueue(self, value):
        self.items.append(value)
        self.sum += value
    
    def dequeue(self):
        if self.items:
            removed = self.items.pop(0)
            self.sum -= removed
            return removed
        raise IndexError("Queue is empty")
    
    def size(self):
        return len(self.items)
    
    def average(self):
        if self.items:
            return self.sum / len(self.items)
        return 0
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)
