"""
x = 2.00000, n = 10

memo = [2, 4, 8, ...]

=====

(2, 10)

(2, 5), (2, 5)

(2, 2), (2, 3), (2, 2), (2, 3)

memo = {2: 4, 3: 8, 5: 32}

=====

Time Complexity: O(n), Space Complexity: O(log n + log n) = O(log n)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.memo = {0: 1}

        return self.calculatePow(x, n)

    def calculatePow(self, x: float, n: int) -> float:
        if n == 1:
            return x

        if n in self.memo:
            return self.memo[n]

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            value = self.calculatePow(x, n / 2) * self.calculatePow(x, n / 2)
        else:
            value = self.calculatePow(x, n // 2) * self.calculatePow(x, n // 2 + 1)

        self.memo[n] = value

        return value


"""
x = 2.00000, n = -2

n < 0

1 / (2, 2)
1 / ((2, 1) * (2, 1))
1 / (2 * 2)

Edge
n < 0
n = 0
"""
