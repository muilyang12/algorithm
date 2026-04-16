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
