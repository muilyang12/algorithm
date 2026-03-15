class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for i in range(n + 1)]

        memo[0] = 1
        memo[1] = 1

        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]


"""
[0, 1, 2]

(N + 2) = N + (N + 1)
"""

"""
In this problem, DP[i] represents the number of ways to reach the i-th step. Since it is possible to arrive from either one step below or two steps below,
the recurrence relation becomes DP[i] = DP[i - 1] + DP[i - 2].
"""
