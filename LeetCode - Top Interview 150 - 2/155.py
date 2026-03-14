class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            _, min_val = self.stack[-1]
            min_val = min(min_val, val)
        else:
            min_val = val

        self.min_val = min_val
        self.stack.append((val, self.min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        val, _ = self.stack[-1]

        return val

    def getMin(self) -> int:
        _, min_val = self.stack[-1]

        return min_val

"""
For this problem, I've almost memorized the technique of storing the `min_val ` so far along with each value. It's become so familiar that I can solve it instantly upon seeing it.
"""
