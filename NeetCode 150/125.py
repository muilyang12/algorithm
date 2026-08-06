class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if not lower_s[left].isalpha() and not lower_s[left].isdigit():
                left += 1
                continue
            if not lower_s[right].isalpha() and not lower_s[right].isdigit():
                right -= 1
                continue

            if lower_s[left] == lower_s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
