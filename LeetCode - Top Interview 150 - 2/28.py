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


"""
sadbutsad
^
"""
