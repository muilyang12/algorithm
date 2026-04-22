"""
The final solution to this problem looks very simple but I struggled with the process of solving it. I think there are two key ideas which are only passing down the amount
that exceeds 1 and initializing memo[0][0] with the total poured amount at the beginning.

It is interesting that this type of approach can also be classified as Dynamic Programming.
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = [[0.0 for _ in range(i + 1)] for i in range(query_row + 1)]
        memo[0][0] = float(poured)

        for i in range(query_row):
            for j in range(i + 1):
                if memo[i][j] > 1:
                    memo[i + 1][j] += 0.5 * (memo[i][j] - 1)
                    memo[i + 1][j + 1] += 0.5 * (memo[i][j] - 1)

                    memo[i][j] = 1

        return memo[query_row][query_glass] if memo[query_row][query_glass] <= 1 else 1


"""
Start from 0?
"""

"""
1
1 1
1 2 1
1 2 2 1
"""

"""
memo

[1]
[1,1]
[0.25,0.5,0.25]
"""
