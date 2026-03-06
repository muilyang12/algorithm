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
