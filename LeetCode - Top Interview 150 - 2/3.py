class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        left = 0
        right = 0

        existing_chars = set()
        while right < len(s):
            if not s[right] in existing_chars:
                existing_chars.add(s[right])
                right += 1
            else:
                existing_chars.remove(s[left])
                left += 1

            result = max(result, right - left)

        return result


"""
abcabcbb
^
^

set()

not s[right] in set

set.add(s[right])
right += 1

in set
set.remove(s[left])
left += 1
"""
