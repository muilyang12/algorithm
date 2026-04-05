"""
There are a few key elements to remember in Dynamic Programming.
1. You must derive the current `memo` value by referencing previous `memo` values. A method where you determine future `memo` values using the current value is not permitted.
2. When setting memo[i], you often need to use functions such as min or max, so you must be cautious when determining the initial values of the memo array.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for _ in range(len(s) + 1)]
        memo[0] = True

        for i in range(1, len(memo)):
            for word in wordDict:
                if i - len(word) < 0:
                    continue

                if not memo[i - len(word)] or s[i - len(word) : i] != word:
                    continue

                memo[i] = True

        return memo[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue

                if s[i - len(word) + 1 : i + 1] == word and not dp[i + 1]:
                    dp[i + 1] = dp[i + 1 - len(word)]

        return dp[-1]
