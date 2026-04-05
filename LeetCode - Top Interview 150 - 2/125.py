class Solution:
    def isPalindrome(self, s: str) -> bool:
        target_chars = list("abcdefghijklmnopqrstuvwxyz0123456789")
        target_chars = set(target_chars)
        s = s.lower()

        filtered = ""
        for char in s:
            if char not in target_chars:
                continue

            filtered += char

        for i in range(len(filtered) // 2):
            if filtered[i] != filtered[len(filtered) - 1 - i]:
                return False

        return True
