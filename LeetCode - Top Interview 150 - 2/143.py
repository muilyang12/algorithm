"""
To perform a reverse operation in a Linked List, there are three fundamental rules to follow.
1. Use only two pointers.
2. Move the pointers after you have changed the direction of the current node's link.
3. However, depending on the specific problem, you might start the previous pointer at None or sometimes at a dummy node.
"""

"""
head = [1,2,3,4,5,6,7,8]
                ^       ^
                      p c
first_left: head.next
last_left: right before slow

first_right: 8
last_right: slow

2 -> 3 -> 4
8 -> 7 -> 6 -> 5

1 8 2 7 3 6 4 5

right_current
left_current

head -> rc -> lc

===

head = [1,2,3,4,5,6,7]
              ^     ^
                    p c

first_left: head.next
last_left: slow

first_right: p
last_right: slow.next
"""


# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        double_end_queue = deque()

        current = head.next

        while current:
            next_node = current.next

            current.next = None
            double_end_queue.append(current)

            current = next_node

        current = head

        while len(double_end_queue) >= 2:
            current.next = double_end_queue.pop()
            current = current.next
            current.next = double_end_queue.popleft()
            current = current.next

        if double_end_queue:
            current.next = double_end_queue.pop()


"""
1, 2, 3, 4, 5, 6, 7, 8

1, 8, 2, 7, 3, 6, 4, 5
"""
