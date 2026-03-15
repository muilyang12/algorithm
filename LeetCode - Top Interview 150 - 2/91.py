class Solution:
    def numDecodings(self, s: str) -> int:
        char_map = {str(i + 1): chr(i + 65) for i in range(26)}

        if len(s) == 1:
            return 1 if s[0] in char_map else 0

        dp = [0 for _ in s]
        dp[0] = 1 if s[0] in char_map else 0
        dp[1] = (dp[0] if s[1] in char_map else 0) + (1 if s[:2] in char_map else 0)

        for i in range(2, len(s)):
            dp[i] = (dp[i - 1] if s[i] in char_map else 0) + (
                dp[i - 2] if s[i - 1 : i + 1] in char_map else 0
            )

        return dp[-1]


"""
chr(): 65 -> "A"
ord(): "A" -> 65
"""
