class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0 for _ in range(len(s) + 1)]

        memo[0] = 1
        memo[1] = 1 if int(s[0]) != 0 else 0

        for i in range(1, len(s)):
            left = memo[i - 1] if 10 <= int(s[i - 1 : i + 1]) <= 26 else 0
            right = memo[i] if int(s[i]) != 0 else 0

            memo[i + 1] = left + right

        return memo[-1]
