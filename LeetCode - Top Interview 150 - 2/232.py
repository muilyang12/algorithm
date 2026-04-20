"""
This problem feels like a perfect twin to "225. Implement Stack using Queues." While you used two queues to implement a stack in that problem, here you are using two stacks
to implement a queue.

This problem is slightly more difficult because, in problem 225, simply moving elements to the other side was enough to mimic a stack, but here, the data must travel from
stack1 to stack2 and then back to stack1 to behave like a queue. It is hard to keep this organized purely in your head. You should definitely simulate the process by putting
in numbers like 1, 2, 3, 4, 5 in the comments below the code to see exactly how the data needs to be moved.
"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack1 and not self.stack2:
            self.stack1.append(x)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            self.stack1.append(x)

            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        if self.stack1:
            return self.stack1.pop()
        elif self.stack2:
            return self.stack2.pop()

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[-1]
        elif self.stack2:
            return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


"""
1, 2, 3, 4, 5


stack1 = [3, 2, 1]
stack2 = [1, 2]
"""
