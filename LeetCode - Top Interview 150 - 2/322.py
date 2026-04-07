class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf for _ in range(amount + 1)]
        memo[0] = 0

        for coin in coins:
            for i in range(coin, len(memo)):
                memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[amount] if memo[amount] != math.inf else -1


"""
amount = 11
[0,1,1,2,2,1,2,2,3,3,2,3]
       ^
"""

"""
This problem is identical to "279. Perfect Squares".

There are two key elements to remember when solving DP problems.
1. The `memo` array should always be filled by referencing previous values to determine the current one. You should not use a method like `memo[i + coin] = memo[i] + ...` to update
future values.
2. It is crucial to set the initial values of the memo array correctly. Since the goal here is to find the minimum value, initializing the memo with math.inf is the best approach.

I used to initialize `memo` array with 0 out of habit. I must keep the above precautions in mind.
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf for _ in range(amount + 1)]
        memo[0] = 0

        for i in range(1, len(memo)):
            for coin in coins:
                if i - coin < 0:
                    continue

                memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[amount] if memo[amount] != math.inf else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf for _ in range(amount + 1)]
        memo[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[amount] if memo[amount] != math.inf else -1


"""
amount = 11
[0,1,1,2,3,1,2,0,0,...]
       ^
"""
