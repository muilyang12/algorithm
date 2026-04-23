class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[False for _ in range(len(p) + 1)] for __ in range(len(s) + 1)]
        memo[0][0] = True

        for j in range(1, len(p)):
            if p[j] == "*":
                memo[0][j + 1] = memo[0][j - 1]

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j]:
                    memo[i + 1][j + 1] = memo[i][j]
                elif p[j] == ".":
                    memo[i + 1][j + 1] = memo[i][j]
                elif p[j] == "*":
                    memo[i + 1][j + 1] = memo[i + 1][j - 1]

                    if s[i] == p[j - 1] or p[j - 1] == ".":
                        memo[i + 1][j + 1] |= memo[i][j + 1]

        return memo[-1][-1]


"""
This problem is truly difficult and I think I need to write the code multiple times to solve it accurately.

There are several important points.
1. You must set initial values before entering the main nested for loops to cover cases where p starts with a pattern like "a*" while nothing is selected from s.
2. In my first attempt I used a while loop to fill True values by moving forward when encountering "*". However DP should determine the current value by looking back at
previous states.
3. When `p[j] == "*"` you must set the initial state using `memo[i + 1][j + 1] = memo[i + 1][j - 1]` which keeps the pointer in `s` the same but moves the pointer in `p`
back two spaces.
4. When p[j] == "*" and the character in s matches the previous character in p you use memo[i + 1][j + 1] |= memo[i][j + 1] to carry over the value from the previous pointer
in s while keeping the pointer in p.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[False for _ in range(len(p) + 1)] for __ in range(len(s) + 1)]
        memo[0][0] = True

        for j in range(1, len(p)):
            if p[j] != "*":
                continue

            memo[0][j + 1] = memo[0][j - 1]

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j]:
                    memo[i + 1][j + 1] = memo[i][j]
                elif p[j] == ".":
                    memo[i + 1][j + 1] = memo[i][j]
                elif p[j] == "*":
                    memo[i + 1][j + 1] = memo[i + 1][j - 1]

                    if p[j - 1] == s[i] or p[j - 1] == ".":
                        memo[i + 1][j + 1] |= memo[i][j + 1]

        return memo[-1][-1]


"""
aab
a*b

[TFTF]
[FTFF]
[FFFF]
[FFFF]
"""