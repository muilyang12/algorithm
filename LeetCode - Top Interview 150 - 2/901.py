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
