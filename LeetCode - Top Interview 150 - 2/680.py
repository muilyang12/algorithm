"""
This problem was quite difficult, even though it is an Easy problem.

In the previous "125. Valid Palindrome" problem I solved it using the `if filtered[i] != filtered[len(filtered) - 1 - i]:` approach to check if the characters at both
ends were the same. It was a very greedy Two Pointers approach.

The basic framework is the same for this problem. However, there was an issue in deciding which pointer to move further when the characters at `left` and `right` do not
match. Since there are cases where `s[left + 1] == s[right]` and `s[left] == s[right - 1]` are both true at the same time, you need to check both the `left + 2` to
`right - 1` and `left + 1` to `right - 2` ranges. To handle this, you can create a helper function to check for palindromes and call it twice, connecting the results
with an `or` condition.

Honestly, thinking of this entire logic from the very beginning seems a bit tough. Therefore, it would be better to run it first, see where it fails, and then fix it.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def is_palindrome(start, end):
            current = 0
            
            while current <= (end - start + 1) // 2:
                if s[start + current] != s[end - current]:
                    return False
                
                current += 1

            return True

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

        return True


"""
No space?
Only alphabet?
Only lowercases?
"""
