"""
It is interesting how these two problems, "232. Implement Queue using Stacks" and "225. Implement Stack using Queues," form a perfect pair.

Both problems require using two Stacks or two Queues, respectively, to simulate the behavior of the other data structure. The difficulty lies in the fact that while one operation
might only require moving elements once, another might require moving them twice to maintain the correct order. Because of this complexity, it is difficult to visualize the movement
logic purely in your head. It is much more effective to actually draw out the shifting logic in the comments.
"""


class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if not self.queue1 and not self.queue2:
            self.queue1.append(x)
        elif self.queue1:
            self.queue2.append(x)

            while self.queue1:
                num = self.queue1.popleft()
                self.queue2.append(num)
        elif self.queue2:
            self.queue1.append(x)

            while self.queue2:
                num = self.queue2.popleft()
                self.queue1.append(num)

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()
        elif self.queue2:
            return self.queue2.popleft()

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        elif self.queue2:
            return self.queue2[0]

    def empty(self) -> bool:
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False


"""
1, 2, 3, 4, 5


queue1 = [3, 2, 1]
queue2 = [4, 3, 2, 1]
"""
