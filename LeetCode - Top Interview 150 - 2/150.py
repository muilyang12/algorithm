class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                second = int(stack.pop())
                first = int(stack.pop())

                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(first / second)
            else:
                stack.append(token)

        return int(stack.pop())
