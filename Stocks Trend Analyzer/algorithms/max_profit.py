class MaxProfit:
    def __init__(self, prices):
        self.prices = prices
    
    def best_interval(self):
        if not self.prices:
            return None, None, 0
        
        min_price = self.prices[0]
        min_index = 0
        max_profit = 0
        buy_day = 0
        sell_day = 0
        
        for i, price in enumerate(self.prices):
            if price - min_price > max_profit:
                max_profit = price - min_price
                buy_day = min_index
                sell_day = i
            if price < min_price:
                min_price = price
                min_index = i
        return buy_day, sell_day, max_profit
