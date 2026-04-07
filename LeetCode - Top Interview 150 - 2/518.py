class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0 for _ in range(amount + 1)]
        memo[0] = 1

        for coin in coins:
            for i in range(coin, len(memo)):
                memo[i] += memo[i - coin]

        return memo[amount]


"""
memo[i] = Count of combination to make i

This problem is quite tricky because you have to correctly determine which loop should be the outer one. You need to decide whether the for loop for memo or the for loop for coins should come first.

To put it more formally, if the problem is about combinations, the coins loop must be on the outside. However, if the problem is about permutations, the coins loop can be on the inside.

Having the coins loop on the outside means you place all the 1s before considering any 2s. You fill in as many 1s as needed, such as (1), (1, 1), or (1, 1, 1), and then add the necessary amount of 2s to get results
like (1, 2) or (1, 2, 2). Once you move on to adding 2s, you can no longer go back and add more 1s because the cycle where `coin = 1` has already finished.
"""
