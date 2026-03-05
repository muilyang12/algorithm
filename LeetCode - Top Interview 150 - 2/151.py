class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.split(r"\s+", s.strip())

        result = [words[-1 - i] for i in range(len(words))]

        return " ".join(result)


"""
"  hello world  "

stript()

"hello world"

split("")

["hello", "world"]
           ^
[w, h]

=====

"hello   world"

split(/\s+/)
"""

"""
The algorithm is very easy. But I need to remember the exact signature of the re.split(reExp, target) function.
"""
