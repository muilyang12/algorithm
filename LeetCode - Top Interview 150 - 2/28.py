class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if (
                i + len(needle) - 1 < len(haystack)
                and haystack[i : i + len(needle)] == needle
            ):
                return i

        return -1


"""
sadbutsad
^
"""

"""
My implementation seemed a bit too simple, so I had a chat with Gemini. I was surprised to learn that comparing strings with == works differently than manually comparing them character-by-character using a for-loop. 

What we call 'Python' is actually CPython by default. Many of its built-in functions are implemented in C, which makes them fast. For example, a built-in like string.find() runs at the C level. Similarly, using == for string comparison in Python compares memory values at the C level, making it significantly faster than iterating through each character in a Python for-loop.

It's definitely clear now. Using haystack[i : i + len(needle)] == needle is much faster than comparing characters one by one in a for-loop. The former 'Beats 20%', while the latter only 'Beats 5%'. It really shows the performance difference.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue

            for j in range(len(needle)):
                if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                    break

                if j == len(needle) - 1:
                    return i

        return -1
