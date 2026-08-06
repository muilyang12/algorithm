class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        counts = {}
        left = 0
        right = 0

        while right < len(s):
            l_char = s[left]
            r_char = s[right]

            counts[r_char] = counts.get(r_char, 0) + 1

            if sum(counts.values()) - max(counts.values()) <= k:
                result = max(result, right - left + 1)
            else:
                counts[l_char] -= 1
                left += 1

            right += 1

        return result
