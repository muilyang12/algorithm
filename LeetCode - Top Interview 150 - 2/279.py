"""
Identical to "322. Coin Change".

There are a few key elements to remember in Dynamic Programming.
1. You must derive the current `memo` value by referencing previous `memo` values. A method where you determine future `memo` values using the current value is not permitted.
2. When setting memo[i], you often need to use functions such as min or max, so you must be cautious when determining the initial values of the memo array.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        possible_squares = []
        current = 1
        while current**2 <= n:
            possible_squares.append(current**2)

            current += 1

        memo = [math.inf for i in range(n + 1)]
        memo[0] = 0

        for i in range(1, len(memo)):
            for square in possible_squares:
                if i - square < 0:
                    continue

                memo[i] = min(memo[i], memo[i - square] + 1)

        return memo[n]
