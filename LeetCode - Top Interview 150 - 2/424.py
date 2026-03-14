class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = -math.inf

        left = 0
        right = 0
        char_counts = {}
        max_count = -math.inf

        while right < len(s):
            if s[right] not in char_counts:
                char_counts[s[right]] = 0

            char_counts[s[right]] += 1
            
            max_count = max(max_count, char_counts[s[right]])
            if (right - left + 1) - max_count > k:
                char_counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1

        return result


"""
Only capital English character?
Only two characters?
"""

"""
s = "AABABBA", k = 2

{} result = 0

AABABBA
!
@
"""

"""
The challenging part here was calculating the sum of all values in the window except for the maximum one. At first, I struggled with this, but the simplest way is to just do sum(window) - max(window).

However, Gemini recommended using current_max = max(current_max, char_counts[s[right]]). Honestly, these kinds of optimizations are hard to come up with on my own, and even after hearing the answer. Because
it feels a bit unintuitive. I felt uneasy, wondering, 'Is it really okay to only check the character at right?'

But if you look closely, the count can only increase through the right pointer. This means the character with the highest count so far can either stay the same or be overtaken by the new element at right.
Since right is the only place where a count can increase, checking only right is perfectly fine. As you know, the core of the Sliding Window algorithm is that elements only enter through right and leave
through left.
"""

"""
In a Sliding Window, you add through right and remove through left. If you recalculate from scratch when moving left, it's not a Sliding Window anymore. Also, the window width should always start at zero
outside the while loop. And, you must update the values first, and then move the left or right pointers.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = -math.inf

        left = 0
        right = 0
        char_counts = {}

        while right < len(s):
            if s[right] not in char_counts:
                char_counts[s[right]] = 0

            char_counts[s[right]] += 1

            counts = list(char_counts.values())
            if sum(counts) - max(counts) > k:
                char_counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1

        return result
