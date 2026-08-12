class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [math.inf for _ in range(amount + 1)]
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue

                memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[-1] if memo[-1] != math.inf else -1
