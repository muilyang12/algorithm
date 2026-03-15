class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for __ in range(m)]

        for i in range(m):
            memo[i][0] = 1
        for i in range(n):
            memo[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]


"""
[
    [1,1]
    [1,2]
]
"""

"""
I find these types of DP problems really challenging. The core of DP is building the next step based on the previous ones, but even after solving quite a lot, the structure doesn't always jump out
at meimmediately.
"""

"""
Honestly, this problem seems very straightforward. I can define DP[i][j] as the number of ways to reach that specific coordinate. Since there are only two ways to arrive at that point, either from
(i-1, j) or (i, j-1), the recurrence relation is simply `DP[i][j] = DP[i - 1][j] + DP[i][j - 1]`.
"""
