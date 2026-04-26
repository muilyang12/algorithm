"""
This problem has a logical structure that is almost perfectly identical to "402. Remove K Digits".

Just as you can compare numbers using `int(stack[-1]) < int(num_char)` remember that characters can also be compared like `"a" < "c"`.

Also in that problem `count < k` was used as one of the conditions for the pop operation. In this problem you must remember that `counts[stack[-1]] > 0` is used as one of the conditions for the pop decision.
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 0

            counts[char] += 1

        stack = []
        stack_set = set()

        for char in s:
            if char in stack_set:
                counts[char] -= 1
                continue

            while stack and stack[-1] > char and counts[stack[-1]] > 0:
                removed = stack.pop()
                stack_set.remove(removed)

            stack.append(char)
            stack_set.add(char)
            counts[char] -= 1

        return "".join(stack)


"""
This problem is quite challenging because it isn't immediately obvious that you should use a Monotonic Stack.

The key idea to remember is checking the remaining count of a character. For example, in "cbacba," when you have "c" in the stack and encounter "b," you check if there are
more "c"s left later in the string. If there are, you can safely pop "c" from the stack because you can add it later.

It seems like monotonic stack problems that involve maintaining order, such as "739. Daily Temperatures" and "503. Next Greater Element II", appear quite frequently.
"""
