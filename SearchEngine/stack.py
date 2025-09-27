# stack.py

class Stack:
    """Custom Stack implementation using list (LIFO)."""

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, x):
        self.items.append(x)
        print(f"[Stack] Pushed: {x}")

    def pop(self):
        if self.empty():
            return None
        val = self.items.pop()
        print(f"[Stack] Popped: {val}")
        return val

    def peek(self):
        return None if self.empty() else self.items[-1]

    def show(self):
        print("Current Stack (top → bottom):", list(reversed(self.items)) if self.items else "Empty")
