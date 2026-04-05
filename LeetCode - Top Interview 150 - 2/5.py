"""
You can think of this as a special case of "647. Palindromic Substrings".
"""


# Time Complexity: O(n^2), Space Complexity: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
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
        result_length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if not memo[i][j]:
                    continue

                if j - i + 1 > result_length:
                    result_length = j - i + 1
                    result = s[i : j + 1]

        return result


# Time Complexity: O(n^2), Space Complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(1, len(s) - 1):
            radius = 1
            while i - radius >= 0 and i + radius < len(s):
                if s[i - radius] == s[i + radius]:
                    if 2 * radius + 1 > len(result):
                        result = s[i - radius : i + radius + 1]

                    radius += 1
                else:
                    break
        
        for i in range(1, len(s)):
            radius = 0
            while i - 1 - radius >= 0 and i + radius < len(s):
                if s[i - 1 - radius] == s[i + radius]:
                    if 2 * radius + 2 > len(result):
                        result = s[i - 1 - radius : i + radius + 1]

                    radius += 1

                else:
                    break

        return result


"""
"babad"

  ^
 ! @

result = 1

"cbbc"
 !@
 !  @
   !@

Edge
""
"a"
"""

"""
The problem isn't that hard. You just need to know how to set a center and keep increasing the radius as long as it stays a palindrome.
"""
