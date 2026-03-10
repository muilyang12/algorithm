class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.before = None
        self.after = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}

        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        target_node = self.hash[key]

        self.remove_node(target_node)
        self.add_to_front(target_node)

        return target_node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove_node(self.hash[key])
            del self.hash[key]

        self.hash[key] = Node(key, value)
        self.add_to_front(self.hash[key])

        if len(self.hash) > self.capacity:
            del self.hash[self.tail.key]
            self.remove_node(self.tail)

    def remove_node(self, node):
        if node.before and node.after:
            node.before.after = node.after
            node.after.before = node.before
        elif node.before:  # The node is tail
            self.tail = node.before
            self.tail.after = None
        elif node.after:  # The node is head
            self.head = node.after
            self.head.before = None
        else:  # Only node
            self.head = None
            self.tail = None

        node.before = None
        node.after = None

    def add_to_front(self, node):
        if self.head:
            node.before = None
            node.after = self.head
            self.head.before = node

            self.head = node
        else:  # Empty
            self.head = node
            self.tail = node


"""
{
    1: Node(1)
    2: Node(2)
    3: 3
    4: 4
}

[2, 3, 1]

Array

O(c)

Linked List

[3, 1, 2]
 !
       @
[1, 2]
 !
    @

=====

Edge Cases

Put [1, 1]
Get [1]
"""

"""
I need to be more intentional about edge cases. The logic involving before and after pointers is where the system is most vulnerable to
failure. Why did I overlook this? I must dive deep into these high-risk areas. Specifically, performing a get or a put at the boundaries
is where the logic is weakest. I need to be more strategic when I'm finding edge cases.
"""

"""
Some operation -> Common

remove_node node
Put node at the head

Easier to maintain
"""
