class StockSpanner:

    def __init__(self):
        self.dp =[]
        
    def calculateConsecutive(self, price):
        weight = 1
        while self.dp and self.dp[-1][0] <= price:
            weight += self.dp.pop()[1]
        self.dp.append((price, weight))
        return weight

    def next(self, price: int) -> int:
        return self.calculateConsecutive(price)