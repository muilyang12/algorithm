class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.tail = None
        self.current_size = 0

    def enQueue(self, value: int) -> bool:
        if self.current_size == self.k:
            return False

        new_node = Node(value)
        if self.current_size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.current_size += 1

        return True

    def deQueue(self) -> bool:
        if self.current_size == 0:
            return False

        if self.current_size == 1:
            self.head = None
            self.tail = None
        else:
            next_node = self.head.next
            self.head.next = None
            self.head = next_node

        self.current_size -= 1

        return True

    def Front(self) -> int:
        if not self.head:
            return -1

        return self.head.val

    def Rear(self) -> int:
        if not self.tail:
            return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.k
