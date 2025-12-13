class ArrayList:
    def __init__(self):
        self.data = []
    
    def append(self, value):
        self.data += [value]
    
    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of bounds")
    
    def size(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def clear(self):
        self.data = []
