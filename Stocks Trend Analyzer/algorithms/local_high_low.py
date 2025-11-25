from dsa.stack import Stack

class LocalHighLow:
    def __init__(self, prices):
        self.prices = prices
    
    def find_local_extremes(self):
        stack = Stack()
        extremes = []
        n = len(self.prices)
        for i in range(n):
            if i == 0 or i == n-1:
                continue
            if self.prices[i] > self.prices[i-1] and self.prices[i] > self.prices[i+1]:
                extremes.append((i, "High", self.prices[i]))
            elif self.prices[i] < self.prices[i-1] and self.prices[i] < self.prices[i+1]:
                extremes.append((i, "Low", self.prices[i]))
        return extremes
