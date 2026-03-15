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
