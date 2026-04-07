# Time Complexity: O(n^2), Space Complexity: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = [[False for _ in range(len(s))] for __ in range(len(s))]
        for i in range(len(s)):
            memo[i][i] = True

            for j in range(1, min(i, len(s) - 1 - i) + 1):
                if s[i - j] != s[i + j]:
                    break

                memo[i - j][i + j] = True

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                continue

            memo[i][i + 1] = True

            for j in range(1, min(i, len(s) - 1 - i - 1) + 1):
                if s[i - j] != s[i + 1 + j]:
                    break

                memo[i - j][i + 1 + j] = True

        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if not memo[i][j]:
                    continue

                result += 1

        return result


"""
[
    [True, False, False], 
    [False, True, False], 
    [False, False, True]
]

[
    [True, True, False], 
    [False, True, True], 
    [False, False, True]
]
"""
