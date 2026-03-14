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

"""
Looking at this problem again, I realized I solved it using a very efficient method a few days ago. I tried to rethink the solution just by reading the problem without looking at my previous code.
This time, I momentarily thought about resetting right to left after incrementing left (`left += 1` and then `right = left`) whenever a duplicate is found. I thought like I had to restart'the scan
from the new left position. However, there's no need to do that. I just need to keep incrementing left until the duplicate is gone. There is absolutely no reason to reset the window to zero.
"""

"""
I don't think I had a perfectly clear grasp of the Sliding Window algorithm before. Looking at what I wrote above

'When I tried to solve it again this time, I attempted to restart the count after moving left. However, looking at my previous implementation, I had done it without a reset. I simply removed what left
through the left side and adding what entered through the right side."

This is the exact same flaw I had in my initial logic for problem 567 (Permutation in String). The essence of the Sliding Window is exactly "The index of the new element entering my scope is right, and
the index of the element leaving is left.". Since the entrance and exit are fixed, the core of the algorithm is to look only at what comes in and what goes out.

"Solving a problem with the Sliding Window method is not just about creating left and right variables. If you create those variables but re-calculate everything inside the window every time, you aren't
truly solving it using the Sliding Window method.
"""
