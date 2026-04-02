class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]

        for i in range(n - 2):
            memo.append(memo[-1] + memo[-2] + memo[-3])
        
        return memo[n]