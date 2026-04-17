"""
At first, I wondered if a stack was even necessary and thought that simply incrementing and decrementing a `count` dictionary would be enough. However, that approach fails to
catch cases like `([)]`, which should return False. The count method cannot filter out these invalid sequences because it only tracks the quantity and not the nesting order.
When a closing bracket appears, the most recently opened bracket must be its matching pair. This rule is absolute, which is why this problem must be solved using a stack to
keep track of the most recent open brackets.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opens = set(["(", "{", "["])

        for parenthesis in s:
            if parenthesis in opens:
                stack.append(parenthesis)
            elif len(stack) == 0:
                return False
            elif parenthesis == ")" and stack.pop() != "(":
                return False
            elif parenthesis == "}" and stack.pop() != "{":
                return False
            elif parenthesis == "]" and stack.pop() != "[":
                return False

        if len(stack) > 0:
            return False

        return True
