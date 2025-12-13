from dsa.array_list import ArrayList

class TrendAnalysis:
    def __init__(self, prices):
        # prices: ArrayList of closing prices
        self.prices = prices
    
    def detect_trends(self):
        trends = ArrayList()
        n = self.prices.size()
        if n == 0:
            return trends
        
        streak = 1
        for i in range(1, n):
            if self.prices.get(i) > self.prices.get(i-1):
                streak = streak + 1 if streak > 0 else 1
            elif self.prices.get(i) < self.prices.get(i-1):
                streak = streak - 1 if streak < 0 else -1
            else:
                streak = 0  # no change
            trends.append(streak)
        return trends
