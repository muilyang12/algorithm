"""
This problem is very similar in approach to "316. Remove Duplicate Letters".

In problem 316 the basic logic was to pop a character if a larger character appeared before it and that larger character existed further down in the string. This problem follows a similar logic where you pop
a number if a larger number appeared before it and you have not yet reached the k limit for removals.

When it comes to stack problems I think the hardest part is actually identifying that the problem should be solved using a Stack.
"""


# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        count = 0

        for n in num:
            while stack and int(stack[-1]) > int(n) and count < k:
                stack.pop()
                count += 1

            stack.append(n)

        while stack and count < k:
            stack.pop()
            count += 1

        start = 0
        while start < len(stack) and stack[start] == "0":
            start += 1
        stack = stack[start:]

        return "".join(stack) if stack else "0"


"""
num = "1432219"

stack = ["1", "2", "1", "9"], "9"
count = 3
"""
