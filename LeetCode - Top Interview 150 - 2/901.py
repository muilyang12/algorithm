"""
[7,2,10,5,12]

stack
[(7,1)]
[(7,1),(2,1)]
[(10,3)]
[(10,3),(5,1)]
[(12,5)]
"""


# Time Complexity: O(n) (n: number of prices, total number of calls)
class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1][0] <= price:
            _, current_span = self.prices.pop()

            span += current_span

        self.prices.append((price, span))

        return span


"""
[7,2,10,5,12]
 !

stack = [(7, 1), (2, 1), (10, 3), (5, 1)]
"""


# Time Complexity: O(n^2) (n: number of prices, total number of calls)
class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)

        result = 0

        for i in range(len(self.prices) - 1, -1, -1):
            if self.prices[i] <= price:
                result += 1
            else:
                break

        return result
