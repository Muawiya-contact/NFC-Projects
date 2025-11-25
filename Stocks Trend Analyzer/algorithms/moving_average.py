from dsa.queue import Queue

class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
    
    def calculate(self, prices):
        q = Queue()
        moving_avgs = []
        for price in prices:
            q.enqueue(price)
            if q.size() > self.window_size:
                q.dequeue()
            moving_avgs.append(q.average())
        return moving_avgs
