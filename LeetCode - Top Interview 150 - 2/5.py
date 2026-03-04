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
